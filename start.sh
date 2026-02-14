echo "Cloning Repo...."
if [ -z $BRANCH ]
then
  echo "Cloning main branch...."
  git clone https://github.com/teamsuraj2/F teamsuraj2/F
else
  echo "Cloning $BRANCH branch...."
  git clone https://github.com/teamsuraj2/F -b $BRANCH /teamsuraj2/F
fi
cd teamsuraj2/F
pip3 install -U -r requirements.txt
echo "Starting Bot...."
python3 main.py
