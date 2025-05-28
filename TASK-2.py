pip install fpdf
import pandas as pd
from fpdf import FPDF

# Load data
df = pd.read_csv("C:/Users/lenovo/OneDrive/Desktop/sales_data.csv")

# Add calculated column
df["Total Sales"] = df["Units Sold"] * df["Unit Price"]

# Analysis
total_units = df["Units Sold"].sum()
total_sales = df["Total Sales"].sum()
best_product = df.groupby("Product")["Total Sales"].sum().idxmax()
region_sales = df.groupby("Region")["Total Sales"].sum()

# Initialize PDF
pdf = FPDF()
pdf.add_page()
pdf.set_font("Arial", "B", 16)
pdf.cell(0, 10, "Sales Summary Report", ln=True, align="C")

pdf.set_font("Arial", "", 12)
pdf.ln(10)
pdf.cell(0, 10, f"Total Units Sold: {total_units}", ln=True)
pdf.cell(0, 10, f"Total Revenue: ${total_sales:.2f}", ln=True)
pdf.cell(0, 10, f"Top Performing Product: {best_product}", ln=True)

pdf.ln(10)
pdf.set_font("Arial", "B", 12)
pdf.cell(0, 10, "Sales by Region:", ln=True)
pdf.set_font("Arial", "", 12)
for region, sales in region_sales.items():
    pdf.cell(0, 10, f"{region}: ${sales:.2f}", ln=True)

# Add detailed table
pdf.ln(10)
pdf.set_font("Arial", "B", 12)
pdf.cell(0, 10, "Detailed Sales Data:", ln=True)
pdf.set_font("Arial", "", 10)

for i, row in df.iterrows():
    text = f"{row['Date']} | {row['Product']} | {row['Region']} | Units: {row['Units Sold']} | Sales: ${row['Total Sales']:.2f}"
    pdf.multi_cell(0, 8, text)

# Output file
pdf.output("sales_report.pdf")
print("PDF report generated: sales_report.pdf")
# to view file location
import os
print(os.getcwd())
