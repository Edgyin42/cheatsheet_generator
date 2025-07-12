import markdown
import fitz


PAGE_LENGTH = 842.0
PAGE_WIDTH = 595.0

def generate_full_html_content(html_body, heading_color): 
    css_styles = f"""
        <style>
            h1 {{
                border: 2px solid #4CAF50;
            }}
            h1, h2, h3, h4, h5, h6 {{
                font-weight: bold;
                color: {heading_color};
            }}
        </style>
        """
    
    return f"""
        <!DOCTYPE html>
        <html>
        <head>
            <meta charset="utf-8">
            {css_styles}
        </head>
        <body>
            {html_body}
        </body>
        </html>
        """


def generator(margin, num_portions, input_path, output_path, heading_color):
    f = open(input_path, 'r')
    html_body = markdown.markdown(f.read())
    
    doc = fitz.open() 
    page = doc.new_page()
    text_rect = []
    rect_width = PAGE_WIDTH // num_portions
    rect = page.rect
    for i in range(num_portions): 
        rect_i = fitz.Rect(rect.x0 + rect_width * i + margin, rect.y0 + margin, rect.x0 + rect_width * (i+1) - margin, rect.y1 - margin)
        text_rect.append(rect_i)
    
    full_html_content = generate_full_html_content(html_body, heading_color)

    for i in range(num_portions): 
        text_height = page.insert_htmlbox(rect = text_rect[i], text = full_html_content)

    doc.save(output_path)
    doc.close()

