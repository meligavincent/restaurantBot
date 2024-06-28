from typing import Any, Text, Dict, List

from rasa_sdk import Action, Tracker
from rasa_sdk.executor import CollectingDispatcher


class ExtractFoodEntity(Action):

    def name(self) -> Text:
        return "action_extract_food_entity"

    async def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:

        food_entity = next(tracker.get_latest_entity_values('food'),None)

        if food_entity :
            dispatcher.utter_message(text=f"Food entity is {food_entity}")
        else:
            dispatcher.utter_message(text="No food entity found")

        return []


class OrderFoodAction(Action):
    def name(self) -> Text:
        return "action_order_food"
    
    async def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        
        dispatcher.utter_message(text="Sure,Which kind of food do you want?")

        return []

class ConfirmOrderAction(Action):
    def name(self) -> Text:
        return "action_confirm_order"
    
    async def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        
        food_entity = next(tracker.get_latest_entity_values('food'),None)
        
        if food_entity:
            dispatcher.utter_message(text=f"Sure, I will order {food_entity} for you.")

        return []