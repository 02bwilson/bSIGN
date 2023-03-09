from cryptography.hazmat.primitives import hashes
from cryptography.hazmat.primitives.asymmetric import rsa, padding

from log import Log


class bSIGN_Signer:

    def __init__(self, mw, mw_flag=True):
        self.mw_flag = mw_flag
        self.log = Log()
        self.signing_algorithm = "SHA256"
        if self.mw_flag:
            self.mw = mw
            self.cur_files = self.mw.cur_files
            self.sign_type_combobox = self.mw.sign_type_combo_box
        else:
            self.cur_files = []
            self.sign_type_combobox = ""


    def sign_files(self):
        if not self.cur_files:
            return

        # Get current
        if self.mw_flag:
            self.signing_algorithm = self.sign_type_combobox.currentText()
        cnt = 1
        size = len(self.cur_files)
        # Sign all the files
        for file_path in self.cur_files:
            self.log.log('Signing file - {}'.format(file_path))
            self.log.log('Generating private key...')
            private_key = rsa.generate_private_key(65537, 2048)
            self.log.log('Private key generated!')
            self.log.log('Reading File...')
            with open(file_path, "rb") as file:
                file_contents = file.read()
            self.log.log('File Read!')
            self.log.log('Generating Hash...')
            if self.signing_algorithm == "SHA256":
                digest = hashes.SHA256()
            elif self.signing_algorithm == "SHA384":
                digest = hashes.SHA384()
            elif self.signing_algorithm == "SHA512":
                digest = hashes.SHA512()
            else:
                raise self.log.log("Invalid signing algorithm!!! {}".format(self.signing_algorithm), "ERROR")
            self.log.log('Hash Generated!')
            self.log.log('Creating signature...')

            signature = private_key.sign(file_contents, padding.PKCS1v15(), digest)
            self.log.log(signature)

            self.log.log('Signature created!...')
            self.log.log('Creating signature file...')
            with open(file_path + '_' + self.signing_algorithm + ".sig", "wb") as signature_file:
                signature_file.write(signature)
            self.log.log('Signature File Created!')
            self.log.log('File {}/{} Complete!'.format(cnt, size))
            cnt += 1
        self.log.log('All files signed!')
