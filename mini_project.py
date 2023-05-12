from enum import Enum


class Pattern(Enum):
    SINGLETON = "Singleton Pattern"
    BUILDER = "Builder Pattern"
    STATE = "State Pattern"
    STRATEGY = "Strategy Pattern"
    OBSERVER = "Observer Pattern"
    COMMAND = "Command Pattern"
    DECORATOR = "Decorator Pattern"
    ADAPTER = "Adapter Pattern"


class DecisionNode:
    def __init__(self, question):
        self.question = question
        self.yes = None
        self.no = None

    def set_yes_node(self, node):
        self.yes = node

    def set_no_node(self, node):
        self.no = node


class PatternGame:
    def __init__(self, root):
        self.root = root
        self.current_node = root

    def start(self):
        while self.current_node is not None:
            print(self.current_node.question)
            answer = self.read_input().lower()
            if answer == "yes":
                self.answer_yes()
            elif answer == "no":
                self.answer_no()
            else:
                print("Invalid input. Please answer 'yes' or 'no'.")

    def answer_yes(self):
        self.current_node = self.current_node.yes

    def answer_no(self):
        self.current_node = self.current_node.no

    @staticmethod
    def read_input():
        return input()


def verify_node(pattern):
    pattern.set_yes_node(DecisionNode("Wohoo! I guessed it! Try again?"))
    pattern.set_no_node(DecisionNode("Oops! Something went wrong! Try again?"))


def main():
    start_game = DecisionNode("Welcome to the game! Think of a design pattern"
                              "and answer as yes or no. Ready?")
    is_flexible = DecisionNode("Does it provide the object creation mechanism"
                               "that enhances the flexibilities of "
                               "the existing code?")
    is_single_instance = DecisionNode("Does it ensure you have at most one"
                                      "instance of a class in "
                                      "your application?")
    is_singleton_pattern = DecisionNode(f"Is it {Pattern.SINGLETON.value}?")
    is_builder_pattern = DecisionNode(f"Is it {Pattern.BUILDER.value}?")
    is_decorator_pattern = DecisionNode(f"Is it {Pattern.DECORATOR.value}?")
    is_adapter_pattern = DecisionNode(f"Is it {Pattern.ADAPTER.value}?")
    is_communication = DecisionNode("Is it responsible for how one class"
                                    "communicates with others?")
    is_mechanism = DecisionNode("Does it provide a mechanism to the context"
                                "to change its behavior?")
    is_behaviour = DecisionNode("Is changing behaviour built into its scheme?")
    is_state_pattern = DecisionNode(f"Is it {Pattern.STATE.value}?")
    is_strategy_pattern = DecisionNode(f"Is it {Pattern.STRATEGY.value}?")
    is_observer_pattern = DecisionNode(f"Is it {Pattern.OBSERVER.value}?")
    is_command_pattern = DecisionNode(f"Is it {Pattern.COMMAND.value}?")
    is_assemble = DecisionNode("Does it explain how to assemble objects and"
                               "classes into a larger structure"
                               "and simplifies"
                               "the structure by identifying"
                               "the relationships?")
    is_notified = DecisionNode("Does it allow a group of objects to be"
                               "notified when some state change")
    is_attach = DecisionNode("Does it attach additional behavior to an"
                             "object dynamically at run-time?")
    oops = DecisionNode("Oops! Something went wrong! Try again?")
    is_end = DecisionNode("End")

    start_game.set_yes_node(is_flexible)
    start_game.set_no_node(is_end)

    is_flexible.set_yes_node(is_single_instance)
    is_flexible.set_no_node(is_communication)

    is_single_instance.set_yes_node(is_singleton_pattern)
    is_single_instance.set_no_node(is_builder_pattern)

    is_communication.set_yes_node(is_mechanism)
    is_communication.set_no_node(is_assemble)

    is_mechanism.set_yes_node(is_behaviour)
    is_mechanism.set_no_node(is_notified)

    is_mechanism.set_yes_node(is_behaviour)
    is_behaviour.set_yes_node(is_state_pattern)
    is_behaviour.set_no_node(is_strategy_pattern)

    is_notified.set_yes_node(is_observer_pattern)
    is_notified.set_no_node(is_command_pattern)

    is_assemble.set_yes_node(is_attach)
    is_assemble.set_no_node(oops)

    is_attach.set_yes_node(is_decorator_pattern)
    is_attach.set_no_node(is_adapter_pattern)

    verify_node(is_singleton_pattern)
    verify_node(is_builder_pattern)
    verify_node(is_state_pattern)
    verify_node(is_strategy_pattern)
    verify_node(is_observer_pattern)
    verify_node(is_command_pattern)
    verify_node(is_decorator_pattern)
    verify_node(is_adapter_pattern)

    game_tree = PatternGame(start_game)
    game_tree.start()


if __name__ == "__main__":
    main()
