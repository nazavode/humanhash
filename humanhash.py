"""
humanhash: Human-readable representations of digests.

The simplest ways to use this module are the :func:`humanize` and :func:`uuid`
functions. For tighter control over the output, see :class:`HumanHasher`.
"""

import operator
import uuid as stduuid
import math
import os


DEFAULT_WORDLIST = (
    'ack', 'alabama', 'alanine', 'alaska', 'alpha', 'angel', 'apart', 'april',
    'arizona', 'arkansas', 'artist', 'asparagus', 'aspen', 'august', 'autumn',
    'avocado', 'bacon', 'bakerloo', 'batman', 'beer', 'berlin', 'beryllium',
    'black', 'blossom', 'blue', 'bluebird', 'bravo', 'bulldog', 'burger',
    'butter', 'california', 'carbon', 'cardinal', 'carolina', 'carpet', 'cat',
    'ceiling', 'charlie', 'chicken', 'coffee', 'cola', 'cold', 'colorado',
    'comet', 'connecticut', 'crazy', 'cup', 'dakota', 'december', 'delaware',
    'delta', 'diet', 'don', 'double', 'early', 'earth', 'east', 'echo',
    'edward', 'eight', 'eighteen', 'eleven', 'emma', 'enemy', 'equal',
    'failed', 'fanta', 'fifteen', 'fillet', 'finch', 'fish', 'five', 'fix',
    'floor', 'florida', 'football', 'four', 'fourteen', 'foxtrot', 'freddie',
    'friend', 'fruit', 'gee', 'georgia', 'glucose', 'golf', 'green', 'grey',
    'hamper', 'happy', 'harry', 'hawaii', 'helium', 'high', 'hot', 'hotel',
    'hydrogen', 'idaho', 'illinois', 'india', 'indigo', 'ink', 'iowa',
    'island', 'item', 'jersey', 'jig', 'johnny', 'juliet', 'july', 'jupiter',
    'kansas', 'kentucky', 'kilo', 'king', 'kitten', 'lactose', 'lake', 'lamp',
    'lemon', 'leopard', 'lima', 'lion', 'lithium', 'london', 'louisiana',
    'low', 'magazine', 'magnesium', 'maine', 'mango', 'march', 'mars',
    'maryland', 'massachusetts', 'may', 'mexico', 'michigan', 'mike',
    'minnesota', 'mirror', 'mississippi', 'missouri', 'mobile', 'mockingbird',
    'monkey', 'montana', 'moon', 'mountain', 'muppet', 'music', 'nebraska',
    'neptune', 'network', 'nevada', 'nine', 'nineteen', 'nitrogen', 'north',
    'november', 'nuts', 'october', 'ohio', 'oklahoma', 'one', 'orange',
    'oranges', 'oregon', 'oscar', 'oven', 'oxygen', 'papa', 'paris', 'pasta',
    'pennsylvania', 'pip', 'pizza', 'pluto', 'potato', 'princess', 'purple',
    'quebec', 'queen', 'quiet', 'red', 'river', 'robert', 'robin', 'romeo',
    'rugby', 'sad', 'salami', 'saturn', 'september', 'seven', 'seventeen',
    'shade', 'sierra', 'single', 'sink', 'six', 'sixteen', 'skylark', 'snake',
    'social', 'sodium', 'solar', 'south', 'spaghetti', 'speaker', 'spring',
    'stairway', 'steak', 'stream', 'summer', 'sweet', 'table', 'tango', 'ten',
    'tennessee', 'tennis', 'texas', 'thirteen', 'three', 'timing', 'triple',
    'twelve', 'twenty', 'two', 'uncle', 'undress', 'uniform', 'uranus', 'utah',
    'vegan', 'venus', 'vermont', 'victor', 'video', 'violet', 'virginia',
    'washington', 'west', 'whiskey', 'white', 'william', 'winner', 'winter',
    'wisconsin', 'wolfram', 'wyoming', 'xray', 'yankee', 'yellow', 'zebra',
    'zulu')


def compress(bytes, target):
    """
    Compress a list of byte values to a fixed target length.

        >>> bytes = [96, 173, 141, 13, 135, 27, 96, 149, 128, 130, 151]
        >>> compress(bytes, 4)
        [64, 145, 117, 21]

    If there are less than the target number bytes, the input bytes will be returned

        >>> compress(bytes, 15)
        [96, 173, 141, 13, 135, 27, 96, 149, 128, 130, 151]
    """

    length = len(bytes)
    if target >= length:
        return bytes

    # Split `bytes` into `target` segments.
    seg_size = float(length) / float(target)
    segments = [0] * target
    # Use a simple XOR checksum-like function for compression.
    for i, byte in enumerate(bytes):
        seg_num = min(int(math.floor(i / seg_size)), target - 1)
        segments[seg_num] = operator.xor(segments[seg_num], byte)

    return segments


def humanize(hexdigest, words=4, separator='-', wordlist=DEFAULT_WORDLIST):
    """
    Humanize a given hexadecimal digest.

    Change the number of words output by specifying `words`. Change the
    word separator with `separator`.

        >>> digest = '60ad8d0d871b6095808297'
        >>> humanize(digest)
        'equal-monkey-lake-beryllium'
    """
    if len(wordlist) != 256:
        raise ValueError("wordlist must have exactly 256 items")
    # Gets a list of byte values between 0-255.
    bytes = tuple(
        map(lambda x: int(x, 16),
            map(''.join, zip(hexdigest[::2], hexdigest[1::2])))
    )
    # Compress an arbitrary number of bytes to `words`.
    compressed = compress(bytes, words)
    # Map the compressed byte values through the word list.
    return separator.join(str(wordlist[byte]) for byte in compressed)
