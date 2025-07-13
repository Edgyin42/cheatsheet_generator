from generator import generator
import argparse
import markdown
import fitz
import pymupdf
import io

def main():
    parser = argparse.ArgumentParser()
    parser.add_argument(
        "-m", "--margin", 
        type = int, 
        default=5
    )
    
    parser.add_argument(
        "-n", "--num-columns", 
        type = int, 
        default=1
    )
    
    parser.add_argument(
        "-o", "--output", 
        type = str, 
        default= "output.pdf"
    )

    parser.add_argument(
        "-i", "--input", 
        type = str, 
        required=True,
    )

    parser.add_argument(
        "-c", "--color", 
        type = str, 
        default="#333333",
    )
    args = parser.parse_args()

    generator(
        margin=args.margin,
        num_columns=args.num_columns,
        input_path=args.input,
        output_path=args.output,
        heading_color=args.color
    )

if __name__ == "__main__":
    main()
    