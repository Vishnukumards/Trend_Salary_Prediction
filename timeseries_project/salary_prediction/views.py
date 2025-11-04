# salary_prediction/views.py (Final Smart Version)

from django.shortcuts import render
import pickle
import os
from django.conf import settings
import pandas as pd
from dateutil.relativedelta import relativedelta

# --- Load historical data ONCE when the server starts ---
# This is much more efficient than reading the file on every request.
try:
    DATA_FILE_PATH = os.path.join(settings.BASE_DIR, 'data', 'price_data.csv')
    historical_data = pd.read_csv(DATA_FILE_PATH, parse_dates=['date'], index_col='date')
except FileNotFoundError:
    historical_data = None

def predict_view(request):
    context = {
        'predicted_price': None,
        'historical_price': None, # New context variable for actual data
        'requested_date': None,
        'error': None
    }
    
    if request.method == 'POST':
        if historical_data is None:
            context['error'] = "Critical Error: Historical data file not found on the server."
            return render(request, 'index.html', context)
            
        try:
            month = int(request.POST.get('month'))
            year = int(request.POST.get('year'))
            
            target_date = pd.to_datetime(f'{year}-{month}-01')
            context['requested_date'] = target_date.strftime('%B %Y')
            
            # --- DECISION LOGIC ---
            
            # The last date we have ACTUAL data for
            last_known_date = historical_data.index.max()

            # Check if the requested date is in our historical data
            if target_date <= last_known_date:
                # --- LOOKUP LOGIC ---
                # Find the row that matches the requested year and month
                actual_value = historical_data[
                    (historical_data.index.year == year) & (historical_data.index.month == month)
                ]
                
                if not actual_value.empty:
                    price = actual_value['avg_monthly_price'].iloc[0]
                    context['historical_price'] = f"₹{price:,.2f}"
                else:
                    context['error'] = f"No historical data found for {context['requested_date']}."

            else:
                # --- PREDICTION LOGIC (for future dates) ---
                delta = relativedelta(target_date, last_known_date)
                steps_to_forecast = delta.years * 12 + delta.months
                
                model_path = os.path.join(settings.BASE_DIR, 'models', 'best_arima_model.pkl')
                
                with open(model_path, 'rb') as f:
                    model = pickle.load(f)

                forecast_all_steps = model.forecast(steps=steps_to_forecast)
                specific_prediction = forecast_all_steps.iloc[-1]
                
                context['predicted_price'] = f"₹{specific_prediction:,.2f}"

        except (ValueError, TypeError):
            context['error'] = "Invalid input. Please select a valid month and year."
        except Exception as e:
            context['error'] = f"An unexpected error occurred: {str(e)}"

    return render(request, 'index.html', context)