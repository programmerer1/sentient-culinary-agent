<p align="center">
  <img src="chef.jpeg"/>
</p>


<h1 align="center">Sentient Chat Agent - Mr. Recipe</h1>

This agent is developed based on https://github.com/sentient-agi/Sentient-Agent-Framework for integration into https://chat.sentient.xyz/. 

Example query:

```bash
{
    "session": 
    {
        "processor_id":"sentient-chat-client",
        "activity_id":"01K6BEMNWZFMP3RMGJTFZBND2N",
        "request_id": "01K6BEPKY12FMR1S19Y3SE01C6",
        "interactions":[]
    }, 
    "query": 
    {
        "id": "01K6BEMZ2QZQ58ADNDCKBPKD51", 
        "prompt": "I have 2 tomatoes, a small piece of yellow cheese, 2 bell peppers, olive oil and eggs in the fridge.", 
        "context": ""
    }
}
```

Response:

```bash
event: SEARCH
data: {"content_type":"atomic.textblock","event_name":"SEARCH","schema_version":"1.0","id":"01K6FTSCNT85ACBB734FTJ25H6","source":"sentient-chat-client","metadata":null,"content":"Thinking about your query..."}

event: response
data: {"content_type":"atomic.textblock","event_name":"response","schema_version":"1.0","id":"01K6FTSNEE7RYQTFBY3CASTDP4","source":"sentient-chat-client","metadata":null,"content":"## Vibrant Veggie and Cheese Frittata\n\n**Servings**: 2-4  \n**Prep Time**: 10 minutes  \n**Cook Time**: 15-20 minutes  \n\nThis sunny frittata is a delightful way to celebrate your fresh produce and eggs, creating a fluffy, colorful dish that's perfect for breakfast, brunch, or a light dinner. It's simple to whip up and bursts with garden-fresh flavors!\n\n### Ingredients\n- 4-6 eggs (adjust based on your supply; I assumed a standard half-dozen for hearty portions)\n- 50g yellow cheese (your small piece, grated or crumbled; like cheddar for a mild tang)\n- 2 tomatoes, diced\n- 2 bell peppers, sliced into thin strips (any color for extra vibrancy)\n- 2 tbsp olive oil\n- Salt and pepper to taste\n- Optional pantry staple: A pinch of dried herbs like oregano if available, for added zest\n\n### Instructions\n1. Preheat your oven to 180°C (350°F) or prepare a stovetop method if you prefer (we'll note it below). In a medium bowl, whisk the eggs with a pinch of salt and pepper until well combined and slightly frothy—about 1 minute.\n2. Heat 1 tbsp of olive oil in a non-stick oven-safe skillet (or regular frying pan) over medium heat. Add the sliced bell peppers and diced tomatoes, sautéing for 4-5 minutes until softened and fragrant, stirring occasionally to release their natural sweetness.\n3. Pour the whisked eggs over the veggies in the skillet, ensuring they spread evenly. Sprinkle the grated cheese on top, letting it melt gently into the eggs. Cook on the stovetop for 3-4 minutes until the edges start to set.\n4. For a fluffy finish, transfer the skillet to the preheated oven and bake for 8-10 minutes, or until the center is just set and the top is golden. (Stovetop alternative: Cover with a lid and cook on low for 5-7 more minutes, checking to avoid overcooking.)\n5. Remove from heat, let it rest for 2 minutes, then slice into wedges. Drizzle with the remaining olive oil for a glossy touch and serve warm.\n\n### Tips\n- Pair with crusty bread or a simple green salad to make it a complete meal—your tomatoes and peppers add natural juiciness!\n- If your cheese is very soft, mix it into the eggs before cooking for even distribution.\n- Leftovers store beautifully in the fridge for up to 2 days; reheat gently in a pan to keep it moist. Enjoy the fresh, wholesome vibes!"}

event: done
data: {"content_type":"atomic.done","event_name":"done","schema_version":"1.0","id":"01K6FTSNEEFZRE0FWKMWEMVY57","source":"sentient-chat-client","metadata":null}↵↵
```
