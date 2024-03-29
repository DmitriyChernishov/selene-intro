from selene import by, have
from selene.support.shared import browser


def test_complete_todo():
    # Given
    browser.open('https://todomvc.com/examples/emberjs/')
    browser.element('#new-todo').type('a').press_enter()
    browser.element('#new-todo').type('b').press_enter()
    browser.element('#new-todo').type('c').press_enter()
    # When
    browser.element('#todo-list>li:nth-of-type(2) .toggle').click()
    # Then
    browser.all('#todo-list>li.completed').should(have.exact_texts('b'))
    browser.all('#todo-list>li:not(.completed)').should(have.exact_texts('a', 'c'))
    browser.all('#todo-list>li').should(have.exact_texts('a', 'b', 'c'))
    # End
    browser.config.quit_driver()