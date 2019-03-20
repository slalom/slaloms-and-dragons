import plot.welcome
import plot.end
import plot.story_factory
import character.creator
import engine.step_handler

def play_step(step, hero):
  step_type = step.get('type')
  if step_type == 'monster':
    engine.step_handler.fight(hero, step)
  if step_type == 'trophy':
    engine.step_handler.pickup(hero, step)

def start():
  plot.welcome.show()
  hero = character.creator.new()
  story = plot.story_factory.generate()
  for step in story:
    play_step(step, hero)
  plot.end.show()
