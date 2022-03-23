python can_pars.py

Check=$(diff real_data.json data.json) 

if [[ $Check == "" ]]
then
    echo 'pass'
else
    echo 'collapse'
fi

coverage run can_pars.py
coverage report