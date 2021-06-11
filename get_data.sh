DATE=$2
CHECK_FOR=$1

while read PIN
do
	echo $PIN
	curl -X GET "https://cdn-api.co-vin.in/api/v2/appointment/sessions/public/findByPin?pincode=$PIN&date=$DATE" -H  "accept: application/json" -H  "Accept-Language: hi_IN" > data.json
	python3 get_data.py $CHECK_FOR
done < pincode.txt


