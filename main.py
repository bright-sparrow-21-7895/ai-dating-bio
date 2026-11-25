# Entry concept: a dating-app bio written as if the AI were honestly
# filling out its own profile. The joke pairs the two things everyone
# suspects about a language model -- it never forgets a word you said,
# yet its "emotional bandwidth" is so small that replies still arrive
# on a corporate 3-5 business day schedule.
import os

ENTRY = "Large language model, small emotional bandwidth. I will remember everything you said and still take 3-5 business days to reply."


def main():
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(ENTRY)


if __name__ == "__main__":
    main()
