echo $1
echo "copy:"
grep $1 -e "M1+c" | wc -l
echo "paste:"
grep $1 -e "M1+v" | wc -l
echo "undo:"
grep $1 -e "M1+z" | wc -l
echo "Delete:"
grep $1 -e "Del" | wc -l
echo "Backspace:"
grep $1 -e "BackSpace" | wc -l
echo "manual ifdef"
grep $1 -e "#if" | wc -l
grep $1 -e "else" | wc -l
grep $1 -e "endif" | wc -l
echo "Copy all"
grep $1 -e "Copy All" | wc -l
echo "Copy current"
grep $1 -e "Copy Current" | wc -l
echo "Enter"
grep $1 -e "key-type Enter" | wc -l
echo "Tab"
grep $1 -e "key-type Tab" | wc -l
grep $1 -e "type-text"
grep $1 -e "type-text" | wc -l