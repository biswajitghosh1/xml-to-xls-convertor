import tkinter as tk
from tkinter import filedialog
import pandas as pd
import logging
import os

# Setup logging
log_file = os.path.join(os.path.dirname(__file__), 'conversion.log')
logging.basicConfig(filename=log_file, level=logging.ERROR,
                    format='%(asctime)s - %(levelname)s - %(message)s')

def browse_xml_file():
    file_path = filedialog.askopenfilename(filetypes=[("XML files", "*.xml")])
    xml_entry.delete(0, tk.END)
    xml_entry.insert(0, file_path)

def convert_to_html():
    xml_file = xml_entry.get()
    if not xml_file.endswith('.xml'):
        result_label.config(text="Please select an XML file.")
        logging.error("No XML file selected.")
        return

    try:
        xml_data = pd.read_xml(xml_file)
        output_file = xml_file.replace('.xml', '.html')
        xml_data.to_html(output_file, index=False)
        result_label.config(text=f"Conversion successful. Output saved as {output_file}.")
    except Exception as e:
        error_msg = f"Error: {str(e)}"
        result_label.config(text=error_msg)
        logging.error(error_msg)

# Create GUI
root = tk.Tk()
root.title("XML to HTML Converter")

# XML file entry
xml_label = tk.Label(root, text="Select XML file:")
xml_label.pack()
xml_entry = tk.Entry(root, width=50)
xml_entry.pack()
browse_button = tk.Button(root, text="Browse", command=browse_xml_file)
browse_button.pack()

# Convert button
convert_button = tk.Button(root, text="Convert to HTML", command=convert_to_html)
convert_button.pack()

# Result label
result_label = tk.Label(root, text="")
result_label.pack()

root.mainloop()