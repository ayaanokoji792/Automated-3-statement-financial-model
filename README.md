# Automated 3-Statement Financial Forecasting Model

## Objective
A dynamic, 5-year financial forecasting model built to project corporate performance using variable growth, margin, and capital expenditure assumptions. The model was initially prototyped in Excel and fully automated using Python (`pandas`, `matplotlib`) to allow for rapid scenario stress-testing.

## Key Features
* **Fully Linked Statements:** Seamless flow of Net Income to Retained Earnings and Cash Flow, ensuring a perfectly balanced sheet under all scenarios.
* **Python Automation:** Utilized `pandas` dataframes to eliminate manual cell-dragging, allowing instant recalculation of multi-year forecasts based on modified arrays.
* **Scenario Analysis:** Configured to easily toggle between "Base Case," "Aggressive Growth," and "Margin Contraction" environments.

## Visual Output
<img width="1000" height="500" alt="chart" src="https://github.com/user-attachments/assets/b12f7bd1-69f7-4aa0-933b-c7ee45133b79" />


## Technical Stack
* **Financial Logic:** Corporate Finance Institute (CFI) Modeling Standards
* **Data Manipulation:** Python (Pandas, NumPy)
* **Visualization:** Matplotlib / Seaborn
* **Prototyping:** MS Excel

## Key Insights Discovered
1. **Margin Sensitivity:** A minor 2% increase in COGS margin severely impacts free cash flow by Year 3, proving the business is highly sensitive to supply chain costs.
2. **Growth vs. Cash:** Aggressive revenue growth scenarios initially drain the cash balance due to heavy working capital and inventory requirements.
