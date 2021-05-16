# bash file to test result for API through curl commands

echo 
echo "------ Get list of trade ------"
echo
echo

curl -i  --output -X GET http://localhost:8000/tradeapi/ 
  
echo
echo "---Create new trade with API---"
echo
echo

curl --header "Content-Type: application/json" \
  --request POST \
  --data '{"unit_price": 500.10, "trd_shares_quantity": 10, "ticker": "TCS", "category": "BUY"}' \
  http://localhost:8000/tradeapi/

echo
echo "---Get shareholder Portfolio---"
echo
echo

curl -i  --output -X GET http://localhost:8000/tradeapi/portfolio/


echo
echo "---Get cumulative return---"
echo
echo

curl -i  --output -X GET http://localhost:8000/tradeapi/return/

