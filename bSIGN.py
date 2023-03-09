import argparse

from signer import bSIGN_Signer

from PyQt6.QtWidgets import QApplication

from mainwindow import bSIGN_MW

if __name__ == "__main__":
    app = QApplication([])
    parser = argparse.ArgumentParser(description='Sign files!')
    parser.add_argument('-f', '--files', nargs='+', help='List the files to sign')
    parser.add_argument('-a', '--hash', help='What hash to use')

    args = parser.parse_args()

    # If using CLI mode
    if args.files or args.hash:
        signer = bSIGN_Signer(None, False)
        signer.cur_files = args.files
        signer.signing_algorithm = args.hash
        signer.sign_files()
    # Else start GUI
    else:
        window = bSIGN_MW()
        window.show()
        app.exec()