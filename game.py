import welcome
import end
import story_factory
import character_creator
import step_engine

def start():
  welcome.show()
  character = character_creator.new()
  story = story_factory.generate()
  for step in story:
    step_type = step.get('type')
    if step_type == 'monster':
      step_engine.fight(character, step)
    if step_type == 'trophy':
      step_engine.pickup(character, step)
  end.show()