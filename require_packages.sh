#!/bin/bash
clear

echo ""
echo -n "[*] Please enter Username : "
read username
echo ""

TMP1=$'\n' tool_list=(`cat ./tool_list.txt`)

for i in ${tool_list[@]}; do
  if [[ "${i}" == *package* ]]
  then
    continue
  else
    `apt-get install -y ${i}`
  fi
done
