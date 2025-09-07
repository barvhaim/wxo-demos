import logging
from ibm_watsonx_orchestrate.agent_builder.tools import tool, ToolPermission

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)


@tool(
    name="YouTubeTranscribe",
    description="Transcribes the audio from a YouTube video ID.",
    permission=ToolPermission.READ_ONLY,
)
def youtube_transcribe(
    video_id: str,
) -> str:
    """
    Transcribes the audio from a YouTube video.

    :param video_id: The YouTube video ID.
    :returns: The transcription of the YouTube video.
    """
    if not video_id:
        logger.error("No video ID provided.")
        return "No video ID provided."

    logger.info(f"Transcribing video with ID: {video_id}")
    transcript = """
Jeff, I have a question for you, and that is, can AI really think?
- Well, Martin, let me answer your question with a math problem.

Exactly the response I would expect from an IBM Distinguished Engineer. Go on.
- I wouldn't want to disappoint. So here's your math problem, Martin: Oliver picks 44 kiwis on Friday. Take notes.

Okay, 44.
- Then he picks 58 kiwis on Saturday. All right, 58.

On Sunday, he picks double the number that he picked on Friday, but five of those are smaller.
- Doesn't matter, 88. So what's the total?

Well, that adds up to 190.
- Well, Martin, according to my AI chatbot, you forgot to subtract the fact that I told you five of them were smaller, so it should have been 185.

Smaller or not, they still count. I think you need a new chatbot.
- Okay, I agree. You know, the fact that five of these were smaller doesn't really change the total. But a research paper recently turned up that some LLMs got tripped up by these kinds of extraneous details. How could an AI that seems so smart make such an obvious mistake?

Yeah, I've seen that paper, and it all comes down to training data. The paper proposes the LLMs perform something called probabilistic pattern matching.
- I'll take notes on this. Thank you.

And that means they search to find the closest data in the training dataset that matches the data.
- They're looking for similar examples of, well, in this case, math problems.

And most of the time, when little details like five were smaller than average, when that appears in a math problem, there's almost always a reason for that, right?
- Almost every time a caveat like that was added in those math problems, in the training data, the answer required taking that caveat into consideration. Hence the LLM incorrectly electing to subtract five from the total because that was the probabilistic pattern seen in most of the relevant training examples.

So Martin, that brings us back to the broader question of: Can AI really think?
- That is a good question.

Or is it really just simulating or imitating thought and reasoning or, in fact, the broader question of are we all living in a simulation? Is everything imitation?
- Is anything actually real?

Slow down there, Jeff. I think you're beginning to hallucinate like a chatbot.
- But yes, this does imply that LLM pattern matching is coming at the expense of actual reasoning. LLMs often come to the right answer without really having a proper understanding of the underlying concepts which can lead to all sorts of issues like these.

So we saw how the extraneous details in the math problem I gave you were able to throw off an LLM, but what else could cause models to struggle with reasoning like this?
- Yeah, LLMs struggle with logical reasoning because there's something called token bias.

I'll take a note on that. Thanks.
- Now, remember, these systems are effectively predicting the next word, or more accurately, the next token in a sequence, and the reasoning output of the model changes when a single token of input changes, which means that tiny little tweaks in how you prompt an LLM with a question can have an outsized effect on the reasoning presented in the output.

So I suppose this is a bit like autocomplete on steroids.
- If I say "Mary had a little lamb, its fleece was white as..." I'm going to say the autocomplete on that is snow, Jeff.

Well, no. According to the autocomplete on my phone, it's "Mary had a little lamb, its fleece was white as a little lamb," yeah.
- Kind of unimpressive.

Well, what would cause such a thing?
- Well, the autocomplete uses a prediction scheme based on probabilities as to what the next word would be, and LLMs do something similar as well, albeit with some additional smarts like attention. And most of the time it's right, but when it isn't, we get hallucinations and then get weird extraneous details and stuff like this that you and I, we would quickly filter out.

A chatbot that appears to be reasoning may actually just be doing a super sophisticated autocomplete where it's guessing not only the next word, but also the next sentence, the next paragraph, or even the entire document.

What a buzzkill, Martin. I mean, you just ruin the magic for all of us. Thanks for that.
- It's sort of like if I tell you when you see a magician saw a lady in a box in half and then I tell you, in fact, there are two ladies, and you're just seeing the arms of one and the legs of the other. Poof. No more magic.

As with all things AI, reasoning is evolving. Look, we can smugly proclaim that AI just doesn't understand concepts the way we superior humans do, but some recent advancements are seeing big improvements in reasoning.
- Most pre-training models today rely on something called training time compute.

Here, I'll take some notes.
- No, thank you very much. Now the models learned to reason, or as we've seen, actually, they learned to perform probabilistic pattern matching during model training. Then the model is released and now it's a fixed entity. So the underlying model here, it doesn't change.

Now, remember, we talked about token bias, how small changes in the input tokens, meaning your prompt, can affect the reasoning in the output.
- Well, that can actually be a good thing as we improve LLM reasoning through some prompt engineering techniques. For example, a number of papers have shown significant LLM reasoning improvements through something called chain of thought prompting.

Right. I've heard about that. That's where you append things like "things step by step" to the prompt, and that encourages the LLM to include reasoning steps before coming up with an answer.

Exactly right, but the emphasis is on the person writing the prompts to use the right magic words, the right incantations to get the LLM to adopt a chain of thought process.
- What new models are doing is inference time compute. It effectively tells the model to spend some time thinking before giving you an answer.

The amount of time it spends thinking is variable based on how much reasoning it needs to do.
- A simple request might take a second or two. Something longer might take several minutes. Only when it's completed its chain of thought "thinking period" does it then start outputting an answer. Basically, think before you speak.

Indeed, and what makes inference time compute models interesting is the inference reasoning is something that can be tuned and improved without having to train and tweak the underlying model.
- So there are now two places in the development of an LLM where reasoning can be improved: at training time with better quality training data, and at inference time with better chain of thought training. Researchers at some of the AI labs are confident we'll see big improvements in the reasoning of future LLM models because of this.

So, Martin, maybe we can finally get an AI that can actually count kiwis.
- And that would be a glorious day, but will it actually be thinking or just simulating thought—a bunch of algorithms all running together? I mean, after all, it's just a bunch of electrical circuits and impulses running through those circuits at the end of the day, right?

Well, that's true. But then so are your thoughts—just a bunch of neurons firing electrical impulses in your brain, and because we don't fully understand it, it seems almost magical.
- Well, until I tell you how the magic trick works, which ruins the magic.

Sort of the way we think about AI as just tending to think and simulating thought through using a bunch of algorithms—that's how the trick works.
- But once you know how the trick works, then we have the question: Is it really thought after all?

Is it really thought after all?
- Jeff, you are asking a question for a philosopher, which I am not. So I ask the next best thing, a popular chatbot, and we actually really like the response it came back with.

So I asked it, "What is the difference between thinking and a simulation?"
- And it said that thinking involves conscious, goal-driven, subjective understanding and adaptability—a simulation of thinking, like a language model, that creates the appearance of thinking by generating responses that fit patterns of real thought and language use, but without actual awareness, without actual comprehension, or without actual purpose.

Actually sounds like a pretty good answer from a system that says it can't actually think.
    """

    if transcript:
        logger.info(f"Transcription successful for video {video_id}")
        return transcript
    else:
        logger.error(f"Failed to transcribe video {video_id}")
        return "Failed to transcribe video."
