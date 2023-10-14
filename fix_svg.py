import argparse
from lxml import etree

def clean_svg(input_file, output_file):
    try:
        parser = etree.XMLParser(recover=True)  # recover from errors
        tree = etree.parse(input_file, parser)
        tree.write(output_file)
        print(f"Cleaned SVG saved as {output_file}")
    except Exception as e:
        print(f"An error occurred: {e}")

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Clean up SVG files.")
    parser.add_argument("-i", "--input", required=True, help="Input SVG file")
    parser.add_argument("-o", "--output", required=True, help="Output SVG file")
    
    args = parser.parse_args()
    clean_svg(args.input, args.output)

