"""
    字符串大小比较逻辑：
        01）在程序中，字符串所用的所有字符都有其对应的 ASC 码，字符串大小的比较起始就是对比其 ASC 码的大小；
        02）字符串是按位比较的，也就是说只要有一位大，那么整体就大；
        03）案例：
            abc 小于 abd
            abc 大于 ab
            Abc 小于 abc（A 的码值为 65，a 的码值为 97）
"""


print(f"abc 小于 abd：{'abc' < 'abd'}")
print(f"abc 大于 ab ：{'abc' > 'ab'}")
print(f"Abc 小于 abc：{'Abc' < 'abc'}")