from enum import Enum


class Links(Enum):
    INITIAL_PAGE_LINK = "INITIAL_PAGE_LINK"
    ES1_PAGE_LINK = "ES1_PAGE_LINK"
    ES2_PAGE_LINK = "ES2_PAGE_LINK"


BASE_LINKS = {
    Links.INITIAL_PAGE_LINK.value: "https://fa.wikipedia.org/wiki/%D9%81%D9%87%D8%B1%D8%B3%D8%AA_%D8%B4%D9%87%D8%B1%D9%87%D8%A7%DB%8C_%D8%A7%DB%8C%D8%B1%D8%A7%D9%86",
    Links.ES1_PAGE_LINK.value: "https://www.namefarsi.com/old-names-of-cities/",
    Links.ES2_PAGE_LINK.value: "http://publicgeography.blogfa.com/post/25"
}
