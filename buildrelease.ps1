conda activate kneeboard_dds_converter

# --paths E:\programme\miniconda\pkgs\openssl-1.1.1l-h8ffe710_0\Library\bin: This allows installer to pack required DDLs like _ssl
pyinstaller.exe -F -y --paths E:\programme\miniconda\pkgs\openssl-1.1.1l-h8ffe710_0\Library\bin ivc_outsiders_patch.py 

rm -r .\build
rm -r .\ivc_outsiders_patch.spec

New-Item -Path ".\" -Name "ivc_outsiders_patch" -ItemType "directory"
Copy-Item .\README.md -Destination ".\ivc_outsiders_patch"
Copy-Item -Path ".\dist\ivc_outsiders_patch.exe" -Destination ".\ivc_outsiders_patch" -Recurse

# & 'C:\Program Files\7-Zip\7z.exe' a -mx9 -sfx .\release\kneeboard_dds_converter.exe kneeboard_dds_converter
 & 'C:\Program Files\7-Zip\7z.exe' a -t7z .\release\ivc_outsiders_patch.7z ivc_outsiders_patch
rm -r ivc_outsiders_patch
