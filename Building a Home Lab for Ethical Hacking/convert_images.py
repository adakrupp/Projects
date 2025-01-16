import re
import sys

def convert_image_links(input_file, output_file):
    # Regular expression to find GitHub image links
    pattern = r'!\[\]\(([^)]+)\)'

    # Read the input file
    with open(input_file, 'r', encoding='utf-8') as f:
        content = f.read()

    # Function to prepend 'Screenshots/' to the image links
    def add_screenshots_folder(match):
        image_link = match.group(1)
        # Prepend 'Screenshots/' to the image link
        image_link = "Screenshots/" + image_link
        return f"![]({image_link})"

    # Perform the replacement
    converted_content = re.sub(pattern, add_screenshots_folder, content)

    # Write the converted content to the output file
    with open(output_file, 'w', encoding='utf-8') as f:
        f.write(converted_content)

    print(f"Conversion complete. New file saved as {output_file}")

if __name__ == "__main__":
    # Check for input file argument
    if len(sys.argv) != 2:
        print("Usage: python convert_images.py <input-file>")
        sys.exit(1)

    # Get the input file from the command line argument
    input_file = sys.argv[1]
    output_file = f"{input_file.rsplit('.', 1)[0]}_converted.md"

    # Call the function to convert the image links
    convert_image_links(input_file, output_file)

