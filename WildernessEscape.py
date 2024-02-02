import random

######
# TREENODE CLASS
######
class TreeNode:
    def __init__(self, story_piece):
        self.story_piece = story_piece
        self.choices = []

    def add_child(self, node):
        self.choices.append(node)

    def traverse(self):
        story_node = self
        print(story_node.story_piece)
        while len(story_node.choices) > 0:
            choice = input("Enter a number choice to continue the story: ")
            if choice not in ["1", "2", "3"]:
                print("Invalid Choice. Please try again!")
            else:
                chosen_index = int(choice)
                chosen_index -= 1
                chosen_child = story_node.choices[chosen_index]
                print(chosen_child.story_piece)
                story_node = chosen_child


######
# VARIABLES FOR TREE
######
story_root = TreeNode("""
    You are in a forest clearing. There is a path to the left.
    A bear emerges from the trees and roars!

Do you: 

1 ) Roar back!
2 ) Run to the left...
3 ) Attack the Bear!
"""
                      )

choice_a = TreeNode("""
    The bear is startled and runs away.

Do you:

1 ) Shout 'Sorry bear!'
2 ) Yell 'Hooray!'
3 ) Run and hide!
"""
                    )
choice_a_1 = TreeNode("""
    The bear returns and tells you it's been a rough week. After making peace with
    a talking bear, he shows you the way out of the forest.

    YOU HAVE ESCAPED THE WILDERNESS.
"""
                      )
choice_a_2 = TreeNode("""
    The bear returns and tells you that bullying is not okay before leaving you alone
    in the wilderness.

    YOU REMAIN LOST.
"""
                      )
choice_a_3 = TreeNode("""
    The bear is disgusted in your fear after yelling at him and leaves you stranded in the wilderness

    YOU REMAIN LOST!
"""
                      )

choice_b = TreeNode("""
    You come across a clearing full of flowers. 
    The bear follows you and asks 'what gives?'

Do you:

1 ) Gasp 'A talking bear!'
2 ) Explain that the bear scared you.
3 ) Shout 'You must not be a real bear if you can speak!'
"""
                    )
choice_b_1 = TreeNode("""
    The bear is unamused. After smelling the flowers, it turns around and leaves you alone.

    YOU REMAIN LOST.
"""
                      )
choice_b_2 = TreeNode("""
    The bear understands and apologizes for startling you. Your new friend shows you a 
    path leading out of the forest.

    YOU HAVE ESCAPED THE WILDERNESS.
"""
                      )
choice_b_3 = TreeNode("""
    The bear is unamused at your ignorance and decides to leave you alone in the wilderness to fend for yourself.

    YOU REMAIN LOST
"""
                      )

choice_c = TreeNode("""
    You have made the wild decision to have a battle with the bear! Should your battling skills not live up to your bravery, 
    there is a good chance that you will be left for dead in the wilderness!
    The bear snarls in rage of your decision and attempts to intimidate you.

Do you:

1 ) Perform a strong attack with your sword!
2 ) Change your mind and run for the hills!
"""
                    )

choice_c_1 = random.randint(1,3)
if choice_c_1 == 1:
    choice_c_1 = TreeNode('''
    You have attempted to swing your sword and strike the bear, but the bear is too strong and has critically slashed you and left you were you stood. 
    Maybe you should have left the bear alone...
    
    YOU HAVE DIED IN THE WILDNESS!
    '''
                          )
else:
    choice_c_1 = TreeNode('''
    The bear was no match for you and your strong sword! You have defeated the bear! 
    Luckily before he died he mumbled the directions to escape the wilderness.
    
    YOU HAVE ESCAPED THE WILDERNESS! 
    '''
                          )
choice_c_2 = random.randint(1,3)
if choice_c_2 == 1:
    choice_c_2 = TreeNode('''
    You have decided that fighting the bear was a bad decision and ran for the hills! 
    Unfortunately, the bear is too fast and chases you through the wilderness, 
    eventually catching up with you and tearing you to shreds!
    
    YOU HAVE DIED IN THE WILDERNESS!
    '''
                          )
else:
    choice_c_2 = TreeNode('''
    Your quick change of mind to not attack the bear was a good decision! 
    You manage to slip away from the bear and stumble across a map to guide you out of the wilderness.
    
    YOU HAVE ESCAPED THE WILDERNESS!
    '''
                          )
story_root.add_child(choice_a)
story_root.add_child(choice_b)
story_root.add_child(choice_c)
choice_a.add_child(choice_a_1)
choice_a.add_child(choice_a_2)
choice_a.add_child(choice_a_3)
choice_b.add_child(choice_b_1)
choice_b.add_child(choice_b_2)
choice_b.add_child(choice_b_3)
choice_c.add_child(choice_c_1)
choice_c.add_child(choice_c_2)

user_choice = input("What is your name? ")
print('\n' + user_choice)

print("Once upon a time...")

story_root.traverse()