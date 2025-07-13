import markdown
import pymupdf

def generate_full_html_content(html_body, heading_color): 
    css_styles = f"""
        <style>
            h1 {{
                border: 2px solid #4CAF50;
            }}
            h1, h2, h3, h4, h5, h6 {{
                font-weight: bold;
                color: {heading_color};
                font: Copperplate;
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


def generator(margin, num_columns, input_path, output_path, heading_color):
    # generate html
    f = open(input_path, 'r')
    html_body = markdown.markdown(f.read())
    full_html_content = generate_full_html_content(html_body, heading_color)
    
    story = pymupdf.Story(html = full_html_content)
    body = story.body
    MEDIABOX = pymupdf.paper_rect("letter")
    WHERE  = MEDIABOX + (margin, margin, -margin, -margin)
    COLS = num_columns
    ROWS = 1
    TABLE = pymupdf.make_table(WHERE, cols=COLS, rows=ROWS)
    CELLS = [TABLE[i][j] for i in range(ROWS) for j in range(COLS)]
    writer = pymupdf.DocumentWriter(output_path) 

    more = 1
    while more: 
        dev = writer.begin_page(MEDIABOX)

        for cell in CELLS: 
            if more: 
                more, _ = story.place(cell)
                story.draw(dev)
        writer.end_page()
    
    writer.close()

