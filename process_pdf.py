def extract_tables_from_pdf(pdf_path):
    import fitz  # PyMuPDF
    import pandas as pd
    
    doc = fitz.open(pdf_path)
    for i, page in enumerate(doc):
        tabs = page.find_tables()
        if tabs.tables:
            for j in range(len(tabs.tables)):
                pd.DataFrame(tabs[j].extract()).to_excel(f'table_{i+1}_{j+1}.xlsx', index=False, header=False)

def extract_images_from_pdf(pdf_path):
    import fitz
    
    doc = fitz.open("test.pdf") # open a document
    
    for page_index in range(len(doc)): # iterate over pdf pages
        page = doc[page_index] # get the page
        image_list = page.get_images()
    
        # print the number of images found on the page
        if image_list:
            print(f"Found {len(image_list)} images on page {page_index}")
        else:
            print("No images found on page", page_index)
    
        for image_index, img in enumerate(image_list, start=1): # enumerate the image list
            xref = img[0] # get the XREF of the image
            pix = fitz.Pixmap(doc, xref) # create a Pixmap
    
            if pix.n - pix.alpha > 3: # CMYK: convert to RGB first
                pix = fitz.Pixmap(fitz.csRGB, pix)
    
            pix.save("page_%s-image_%s.png" % (page_index, image_index)) # save the image as png
            pix = None
