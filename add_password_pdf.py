# !!! RUN IN TERMINAL !!!
from PyPDF2 import PdfFileReader, PdfFileWriter
from getpass import getpass
from pathlib import Path


def protected_pdf(path, method='encrypt'):
    if method == 'encrypt':
        pdf = PdfFileReader(f'{path}')
        pdf_writer = PdfFileWriter()

        for page in range(pdf.numPages):
            pdf_writer.add_page(pdf.pages[page])

        password = getpass(prompt='Enter password: ')
        pdf_writer.encrypt(password)

        with open(f"{path.stem}_protected.pdf", 'wb') as file:
            pdf_writer.write(file)

        print('Passwords protected PDF file is successfully created.')

    elif method == 'decrypt':
        password = getpass(prompt='Enter password: ')
        reader = PdfFileReader(f'{path}')
        writer = PdfFileWriter()

        if reader.is_encrypted:
            reader.decrypt(password)

        for page in reader.pages:
            writer.add_page(page)

        with open(f"{path.stem}_unprotected.pdf", "wb") as f:
            writer.write(f)

        print('Unprotected PDF file is successfully created.')


if __name__ == '__main__':
    pdf_path = Path('pdf_filename') # instead pdf_filename must be your name of pdf file
    protected_pdf(pdf_path)

    # pdf_path = Path('pdf_protected_filename') # instead pdf_protected_filename must be your name of protected pdf file
    # protected_pdf(pdf_path, method='decrypt')
