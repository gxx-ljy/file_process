def extract_images_from_pdf(pdf_path):
    import fitz  # PyMuPDF
    import pandas as pd
    
    doc = fitz.open(pdf_path)
    for i, page in enumerate(doc):
        tabs = page.find_tables()
        if tabs.tables:
            for j in range(len(tabs.tables)):
                pd.DataFrame(tabs[j].extract()).to_excel(f'table_{i+1}_{j+1}.xlsx', index=False, header=False)
