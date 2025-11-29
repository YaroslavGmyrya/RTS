iteration=0
max_iteration=1000

prog="jitter_benchmark"

test_file1="default_test.txt"
test_file2="noise_test.txt"
test_file3="affinity_test.txt"
test_file4="affinity+noise_test.txt"

sudo ./$prog > $test_file1
sudo ./$prog 2 > $test_file2

sudo ./src/noise.sh > /dev/null 2>&1 &
sleep 5

sudo ./$prog > $test_file3
sudo ./$prog 2 > $test_file4

kill $!

python3 parser.py $test_file1
python3 parser.py $test_file2
python3 parser.py $test_file3
python3 parser.py $test_file4