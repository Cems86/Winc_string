# Do not modify these lines
__winc_id__ = '71dd124b4a6e4d268f5973db521394ee'
__human_name__ = 'strings'

# Add your code after this line
score_0='Ruud Gullit'
score_1='Marco van Basten'
goal_0=int(32)
goal_1=int(54)

scorers=f"{score_0} {goal_0}, {score_1} {goal_1}"
report=f'{score_0} scored in the {goal_0}nd minute\n{score_1} scored in the {goal_1}th minute'

player='Ronald Koeman'
first_name=player[:player.find(" ")]
last_name= player[player.find(" "):][1:] 
last_name_len=len(last_name)
name_short=f'{first_name[0]}. {last_name}'

chant=(len(first_name)* f'{first_name}! ') [:-1]
good_chant=chant[:-1]!=str(' ')
chant_l=len(chant)
print(good_chant)
print (first_name)
print (last_name)
