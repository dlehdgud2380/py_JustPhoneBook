#Telephone Book by Scoutlee

import time

class imfomation:

    def name(self, def_name):
        self.name = def_name

    def phone(self, def_phonenumber):
        self.phone = def_phonenumber

print("PHONEBOOK by ScoutLee\n")

program_start = 1

PhoneBook = {}

while  program_start == 1:

    method =int(input("\n\n\n하실 작업을 선택하세요.\n\n(1)주소록 추가\n(2)주소록 수정\n(3)주소록 삭제\n(4)주소록 검색\n(5)등록된 주소록 확인\n(6)주소록 TXT파일로 저장\n번호입력: "))

    if method == 1:

        IMFORM = imfomation()

        IMFORM.name(input("\n이름을 입력해주세요: "))

        if IMFORM.name in PhoneBook :
            print("\n중복된 이름이 있습니다. 자동적으로 (2)이런식으로 구분이 됩니다.\n")
            IMFORM.name = IMFORM.name + "(2)"
        else:
            pass

        try:
            IMFORM.phone(int(input("전화번호를 입력해주세요: ")))
        except ValueError:
            print("\n\n숫자를 입력해주세요!\n\n")
            PhoneBook.update({IMFORM.name:IMFORM.phone})
            del PhoneBook[IMFORM.name]
        else:
            PhoneBook.update({IMFORM.name:IMFORM.phone})
             #PhoneBook[IMFORM.name]= IMFORM.phone

        print("\n수정된 주소록 목록: %s" %PhoneBook)
        time.sleep(1.5)

    elif method == 2:

        print("\n\n%s\n" %PhoneBook)

        IMFORM = imfomation()

        IMFORM.name(input("\n수정하실 주소록이름을 입력해주세요: "))
        IMFORM.phone(int(input("수정할 전화번호를 입력해주세요: ")))

        PhoneBook.update({IMFORM.name:IMFORM.phone})

        print("\n수정된 주소록 목록: %s" %PhoneBook)
        time.sleep(1.5)

    elif method == 3:

        print("\n\n%s\n" %PhoneBook)

        IMFORM = imfomation()

        del_mode=input("삭제할 주소록 이름을 입력해주세요: ")

        del PhoneBook[del_mode]

        print("\n수정된 주소록 목록: %s" %PhoneBook)
        time.sleep(1.5)

    elif method == 4:

        seach_mode =input("\n검색할 주소록 이름을 입력해주세요: ")

        if seach_mode in PhoneBook:

            print("\n주소록에 있습니다.")

        else:

            print("\n주소록에 없습니다.")

        time.sleep(1.5)

    elif method == 5:

        print("\n현재 등록되어 있는 주소는 다음과 같습니다.\n")

        name_in_phonebook = []
        number_in_phonebook = []

        for i in PhoneBook:
            name_in_phonebook.append(i)

        for j in PhoneBook.values():
            number_in_phonebook.append(j)

        for open_phonebook in range (0, len(PhoneBook)):
            print("(%d)%s: %d" %(open_phonebook+1, name_in_phonebook[open_phonebook], number_in_phonebook[open_phonebook]))

        time.sleep(1.5)

    elif method == 6:

        ContactFile = open("Contact.txt", 'w')

        name_in_phonebook = []
        number_in_phonebook = []

        for i in PhoneBook:
            name_in_phonebook.append(i)

        for j in PhoneBook.values():
            number_in_phonebook.append(j)

        for open_phonebook in range (0, len(PhoneBook)):
            data = "(%d)%s: %d" %(open_phonebook+1, name_in_phonebook[open_phonebook], number_in_phonebook[open_phonebook])
            ContactFile.write(data)

        ContactFile.close()

        print("\n연락처가 py프로그램이 위치한 폴더에 저장되었습니다.\n")
        time.sleep(1.5)


























