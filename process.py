# importing the necessary libraries
import os
import fitz


file_path = "c2cy20348k_bulk.pdf"
pdf_file = fitz.open(file_path)
location = "tests1"
# Reading the location where to save the file
if not(os.path.exists(location)):
    os.mkdir(location)


# finding number of pages in the pdf
number_of_pages = len(pdf_file)
print("Working")
# iterating through each page in the pdf
for current_page_index in range(number_of_pages):
    count = -1
    # iterating through each image in every page of PDF
    for img_index, img in enumerate(pdf_file.get_page_images(current_page_index)):
        count += 1
        xref = img[0]
        image = fitz.Pixmap(pdf_file, xref)
        if image.colorspace is None:
            image.save("{}/image{}-{}.png".format(location, current_page_index, img_index))

        elif image.colorspace not in (fitz.csGRAY.name, fitz.csRGB.name):
            print(image.colorspace)
            image = fitz.Pixmap(fitz.csRGB, image)

            image.save("{}/image{}-{}.png".format(location, current_page_index, img_index))

            print('image.colorspace not in (fitz.csGRAY.name, fitz.csRGB.name)')
        # if it is a is GRAY or RGB image
        elif image.n < 5:
            image = fitz.Pixmap(fitz.csRGB, image)
            image.save("{}/image{}-{}.png".format(location, current_page_index, img_index))
        # if it is CMYK: convert to RGB first

        else:
            new_image = fitz.Pixmap(fitz.csRGB, image)
            new_image.save("{}/image{}-{}.png".foramt(location, current_page_index, img_index))


out = open("out.txt", "wb")  # open text output
for page in pdf_file:  # iterate the document pages
    text = page.get_text().encode("utf8")  # get plain text (is in UTF-8)
    out.write(text)  # write text of page
    out.write(bytes((12,)))  # write page delimiter (form feed 0x0C)
pdf_file.close()
