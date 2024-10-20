# https://pymupdf.readthedocs.io/en/latest/textpage.html#TextPage.extractDICT

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




def split_pdf_vertically(doc, n1=0, n2=0, start_page=15, end_page=None):
    """
    根据页面高度裁剪页眉和页脚
    将PDF文档垂直分割成多个部分。
    左上角是坐标原点

    参数:
    doc: 输入的PDF文档对象。
    n1: 顶部裁剪的高度，默认为0像素。
    n2: 底部裁剪的高度，默认为0像素。
    start_page: 开始裁剪的页码，默认从第15页开始。
    end_page: 结束裁剪的页码，默认为None，表示裁剪到文档末尾。

    返回:
    一个新的PDF文档对象，其中包含了裁剪后的页面。
    """
    import fitz

    # 获取输入文档的总页数
    total_pages = doc.page_count
    
    # 打开一个新的PDF文档，用于存放裁剪后的页面
    new_doc = fitz.open()

    # 遍历输入文档的每一页
    for page in doc:
        # 获取当前页面的宽度和高度
        width = page.rect.width
        height = page.rect.height

        # 如果没有指定结束页码，则将结束页码设置为总页数
        if not end_page or end_page > total_pages:
            end_page = total_pages
        
        # 检查当前页面是否在裁剪的页码范围内
        if start_page - 1 <= page.number < end_page:
            # 创建一个新的页面，高度为原页面高度减去裁剪的高度
            new_page = new_doc.new_page(width=width, height=height - n1 - n2)
            # 在新页面上显示裁剪后的原页面内容
            new_page.show_pdf_page(new_page.rect, doc, page.number, clip=fitz.Rect(0, n1, width, height - n2))
        else:
            # 如果当前页面不在裁剪范围内，跳过此页面
            continue

    # 返回包含裁剪后页面的新PDF文档
    # return new_doc
    if False:
        output_pdf = "test.pdf"
        new_doc.save(output_pdf)
    return new_doc
