from selene import by, be, have
from selene.support.shared import browser


def test_complete_todo():
    # open TodoMVC page
    browser.open('https://todomvc.com/examples/emberjs/')

    # add todos: 'a', 'b', 'c'
    # todos should be 'a', 'b', 'c'
    browser.element(by.id('new-todo')).type('a').press_enter()
    browser.element(by.id('new-todo')).send_keys('b').press_enter()
    browser.element(by.id('new-todo')).type('c').press_enter()

    browser.all('#todo-list>li').should(have.exact_texts('a', 'b', 'c'))

    # toggle 'b'
    browser.all('#todo-list>li').element_by(have.exact_text('b')).element('.toggle').click()


    # completed todos should be b
    browser.all('#todo-list>li').element_by(have.css_class('completed')).should(have.exact_text('b'))
    browser.all('#todo-list>li: last-child').element_by(have.exact_text('b'))

    # active todos should be a, c
    browser.all('#todo-list>li').element_by(have.no.css_class('completed')).should(have.exact_texts('a', 'c'))