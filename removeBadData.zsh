cd raw
for f in *.pcm
do 
	ffmpeg -f s16le -y -ar 44.1k -ac 1 -i $f $f.wav;
	afplay $f.wav 
	grep $f -i ../train_list.csv
	echo "Do you wish to keep it?"
	afplay $f.wav
	select yn in "Yes" "No"; do
    		case $yn in
        		Yes ) echo Yes; break;;
        		No ) echo $f >> ../to_remove.csv; break;
    		esac
	done
done
cd ..
