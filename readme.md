Contacts parser to vcf file
=============================

Быстрый старт
-----------

Запускать командой:

        python contacts_parser.py contacts_test.xml

Выходные файлы будут появлятся в директории out

Пример, на входе contacts_test.xml:

    <?xml version="1.0" encoding="UTF-8"?>
    <root>
        <contacts>
            <contact>
                <vcard>BEGIN:VCARD
    VERSION:3.0
    PRODID:-//R//R//EN
    UID:345231fe-bd72-11ef-920e-19889846a244
    FN;CHARSET=UTF-8:Баланс
    N;CHARSET=UTF-8:;Баланс;;;
    ORG;CHARSET=UTF-8:МТС;;
    TEL;TYPE=CELL:*100#
    END:VCARD
    </vcard>
                <workspace>personal</workspace>
            </contact>
    </root>

На выходе 1.Баланс.vcf:

    BEGIN:VCARD
    VERSION:3.0
    PRODID:-//R//R//EN
    UID:345231fe-bd72-11ef-920e-19889846a244
    FN;CHARSET=UTF-8:Баланс
    N;CHARSET=UTF-8:;Баланс;;;
    ORG;CHARSET=UTF-8:МТС;;
    TEL;TYPE=CELL:*100#
    END:VCARD