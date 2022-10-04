# Testing Python Applying Unit Testing, TDD, BDD and Acceptance Testing by David Sale

## 1. A History of Testing
## 2. Writing Unit Tests
## 3. Utilizing Unit Test Tools
## 4. Writing Testable Documentation
## 5. Driving Your Development with Tests
## 6. Writing Acceptance Tests
## 7. Utilizing Acceptance Test Tools
## 8. Maximizing Your Code's Performance
## 9. Looking After YOur Lint
## 10. Automating Your Processes
## 11. Deploying Your Application
## 12. The Future of Testing Python

---
---

# 1. A History of Testing

## Introduction

THE IDEA OF testing is one that has evolved over many years in the development community. Developers used to have much less focus on testing up front and just wrote code and dealt with any problems that arose by quickly writing fixes after a testing period at the end of a project. That isn’t to say that there weren’t developers out there who were writing code that was trouble free when out in the wild, but on the whole, writing code without tests in general is going to lead to problems down the line. There were also cases where testing was a priority, such as code that could cause destruction or the possibility of a person dying. In such circumstances there would be rigorous testing, but this was very much the exception rather than the rule.

The first real change in ideology came with improvements in technology and the resulting development pressures that came with it. When computers were slower, code modification cycles took much longer. Even a simple program could take tens of minutes to build, and large projects could take hours. This resulted in a batch development process where people spent a great deal of time pouring over code, figuring out issues, and then making sets of changes. The amount of time spent verifying changes to the code was comparatively small compared with the cycle time.

As computers became faster, compilation times shrank and development cycle times correspondingly shrank. It became feasible to make small changes to code, quickly build the product, and then verify the results of those few changes. This meant that code was written and tests covered that code to ensure it behaved as expected. Also, as computer systems became more powerful, the complexity of software increased. Even a simple program these days often has both a client and server component running on different systems (such as a browser and web server). Operating systems offer a bewildering variety of services to a program. Choreographing these interactions requires managing complexity in a systematic way. Features of Python such as loose typing impose additional verification demands on developers, as errors in coding cannot be caught at a compilation stage. Similarly, because Python has no demands on the type of objects it is manipulating, you can end up with strange behavior if you have not handled all cases correctly.

Testing forces developers to think about the code that they are writing and consider all sorts of different scenarios and the outcomes rather than focusing on the happy path scenario that takes into account only how the code should be used. When combined with a test driven development approach (TDD; see Chapter 5), this ideology ensured that testing was baked in to the development process and not a tedious afterthought. One of the worst traps a developer can fall into is writing a bunch of code and then going back and testing it all at the end. Not only is this approach more time consuming and often rushed, but it also means revisiting code that isn’t fresh in the mind like it was at the time of writing. When you revisit the method to write a test, the context and thought process at the time of writing is often lost to you.

Similarly, the change from the waterfall development processes to agile has brought a huge focus on testing while developing rather than treating testing as an afterthought, as I describe previously. Agile development advocates that teams include dedicated quality assurance (QA) personnel, whose sole focus is to write tests and maintain a solid test suite around the application. This allows someone who hasn’t written the code to look at it from a fresh angle and perhaps spot weaknesses or bugs in the code before those glitches reach the customer.

Following on from TDD, agile development also spawned the concept of behavior driven development (BDD; see Chapter 6). This method takes unit testing one step further and looks to test the application’s behavior in terms of functionality being delivered. BDD is also known as an acceptance test and generally comes in the form of a human readable feature file, which describes the functionality and then maps to step files, which execute the test code underneath. The huge benefit of this approach is that non-technical team members, such as a scrum master (person responsible for removing impediments that arise in a team and assists in organizational matters) or product owner (person wanting the deliverable and setting the requirements for the project), can write feature files, and then the developer or QA can implement the code underneath. With this setup in place, you basically have testable documentation for your system that anyone on the team can understand. This approach also allows you to create a failing acceptance test that you develop your code to pass, ensuring that you deliver the feature you have set out to create. Unit testing alone does not produce such reliable results. It is the combination of the two testing practices that ensures you can deliver quality software and be confident when it goes live.

Clearly, the mindset of developers has changed over the years from not just writing code but to ensuring that their code is tested from all angles. From unit testing to acceptance testing, Python developers have implemented libraries and tools to help Python developers follow these changes to the development process. This book covers their implementation and usage so that you too can get up to speed on the latest testing tools and techniques to ensure you are not left stuck in the past of testing history.

## You Do Test, Don’t You?

A huge shift has occurred in recent years of software development toward testing and ensuring that your application delivers absolute quality. With the advent of social networks and the ever-increasing pressure of media attention, defects in your code could be costly to both you and your reputation or that of any company you may represent. Whether it be security flaws exposing sensitive customer data, defects that allow hackers access to deface your website, or simply a payments page failing to execute orders, errors can cost your business huge sums of money.

Don’t think of problems on only the large-scale, either. Without a proper testing suite in place, how do you know you have delivered the functionality you set out to deliver at the beginning of writing code? Take a simple data submission form. You have coded the fields to accept a name, address, and e-mail, without any testing. You quickly enter the data as expected and your submit works fine. But what if your customers enter something you didn’t expect in the fields—for instance, a number in the name field? Does your code handle this? What if you make changes to the code? Are you sure that the program still functions as it should?

You can see some of the problems developers face when writing code of this nature and how testing can give you a repeatable process that ensures you are delivering working software every time. Luckily for you, this shift in mindset to place such importance in testing has spawned numerous, quality testing tools and frameworks to make the process as simple as possible.

You can certainly make great code without tests. In fact, it is highly likely that many software houses put out software without rigorous testing. The key advantage of writing tests, especially as part of the development process, is that testing gives you confidence in your code before it goes live. As a developer, you are often on call to support your applications in the middle of the night. Do you really want that phone call at 3 a.m. because you didn’t write tests to cover that edge case? Testing won’t stop this from ever happening again, but it will make it a very rare occurrence. You will have good knowledge of the different routes through your system, making it easier to debug the situations where the worst may happen.

# 2. Writing Unit Tests

## What Is Unit Testing?

In unit testing, you look to cover the application’s functionality at its most basic level. Test each individual unit of code, typically a method, in isolation to see if given certain conditions it responds in the expected way (see Figure 2-1). Breaking testing down to this level gives you confidence that each part of the application will behave as expected and enables you to cover edge cases where the unexpected happens and deal with them accordingly.

![Figure](ScreenshotsForNotes/Chapter2/Figure_2_1.PNG)

In the preceding example, the methods highlighted are the individual units of this application that you need to test. If you know that each of the calculate class’s methods work as expected, you can be confident that the calculate feature of your application has been delivered to your expectations.

For instance, you may wish to test whether the result of calling the method with two numbers actually adds them together to produce the correct sum. Breaking your code down into these units makes the testing process easier. When dealing with a small unit of an application, you have a clear understanding of its responsibilities and the things that can go wrong with the specific piece of code, thus enabling you to cover the unit with the appropriate tests.

Furthermore, when testing in this manner it usually becomes obvious if you have broken down the code into a good-sized unit. If you have to write many different tests to cover all the different possibilities that the method can go through, your method may be too large and you should consider refactoring it into two or more methods with fine-grained responsibilities. Conversely, there may be cases where your method is too simple and could be combined with some other functionality to create a more useful method. As a programmer with experience, you should start to get a feel for a good-sized method. Ten lines is often a good rule of thumb to follow. There are, of course, plenty of cases where you need more or less than this arbitrary number of lines, and as a programmer your common sense should guide you to provide the most readable code.

The tests that you write are a story that explains your code. What would you want to read or see when first reading through the code and trying to understand what it does? Clear, concise naming conventions of variables, class names, filenames, and tests can all help to make your code clear and easy to maintain for other people.

Testing and, in particular, test driven development (TDD; see Chapter 5), can really help to achieve these goals. TDD forces you to think about your code, and in this moment of careful consideration you can take into account the needs of the application, the design of the code, and how other programmers will interpret your intentions. Use testing to your advantage to make your code cleaner and more efficient. With a good test suite in place, refactoring is easy because you know when you change your code you haven’t broken any previous behavior. The tests take the guesswork out of your development process and you can deliver great applications, knowing you have delivered something robust and reliable.

## What Should You Test?

A question that many developers ask especially when first starting out is, what should I test? This is an interesting question and also a fair one, as the applications that are being built now are often vast with many complexities. However, unit testing makes the task easier as the whole idea is to focus on the smallest units of code rather than thinking about how to test the large application you are putting together as a whole. Before you write any code you give thought to the kind of tests you will be writing to check the methods will work as expected. As you write more and more unit tests you will gain experience in what works well and what perhaps causes you issues later down the line. For example, a frequent mistake of inexperienced developers is writing very brittle test suites. This means that as code evolves the tests break for reasons other than the functionality changing. The tests are often checking elements of the code or data to too fine a granularity, meaning that as data changes (and not your functionality, which is what you are really testing), the tests fail and you need to go and fix it. Making your tests as flexible as possible while still testing your functionality is the best way to defend against this brittleness.

Another reason to test comes from the process of finding bugs whether in a production environment, the test environment, or while testing your application locally. Whenever you find a bug that affects your application that requires a code change to fix, you should write a test to cover that scenario. By doing this, you ensure that you have covered the defect that caused the problem and with test in place the bug should not reoccur in the future. By adding this layer of defense every time you find a bug (hopefully, not very often) you ensure that your code is more robust in the future as more functionality is added.

## Writing Your First Unit Test

By now, you are probably eager to start writing your first unit test. Perhaps you have written tests before but are looking for a refresher in how to write good, concise unit tests. Whatever your Python or testing background, let’s start at the beginning with some simple tests for a straightforward application. The examples first show you how to structure your test into a class with the correct naming conventions. Further on in the chapter, you are simply shown snippets of test methods, which you are expected to use with a proper test class.

One of the classic examples for demonstrating unit testing is a small calculator program. Python actually includes a lot of basic math functionality in the standard library. But what if you wrapped that into a simple-to-use command line application that could perform some simple calculations? This first scenario demonstrates how to implement the calculate class of the application example from earlier. Start with the add method, which looks something like this.

```Python3
class Calculate():
    def add(self, x: int, y: int) -> int:
        if type(x) == int and type(y) == int:
            return x + y
        else:
            raise TypeError("Invalid type: {0} and {1}".format(type(x), type(y)))


if __name__ == '__main__':
    calc = Calculate()
    result = calc.add("Hello", "World")
    print(result)
```

Clearly, this is a very simple class that is just making use of Python’s built-in math function for adding and making it into a method you can call in your code. Save this code to a file named calculate.py, then execute this and see the result, like so.

```
$ python calculate.py
4
```

## Checking Values with the assertEquals Method

You have some working code, so why not write the tests to prove it and look into what could go wrong if the code is used in ways you didn’t foresee? Try writing a test that checks to see that if you pass in the two numbers as 2, then you get the result as 4. Using the standard Python library, you can import the unittest package. This provides useful methods to make different kinds of assertions (for instance, checking whether something meets some condition) on your method. One of those assertions you can use is the assertEqual method. This method allows you to pass in two values and check whether they are equal.

Create a test file called calculate_test.py, following the standard naming conventions of using the class name under test and appending with _test.

```Python3
import unittest
from calculate import Calculate


class TestCalculate(unittest.TestCase):
    def setUp(self) -> None:
        self.calc = Calculate()

    def test_add_method_raises_typeerror_if_not_ints(self):
        self.assertRaises(TypeError, self.calc.add, "Hello", "World")

    def test_add_method_returns_correct_result(self) -> None:
        self.assertEqual(4, self.calc.add(2, 2))


if __name__ == '__main__':
    unittest.main()
```

A line-by-line examination shows that this example first imports the functionality you need from Python’s unittest module. You are also importing your own class, Calculate, so that you can test its methods. You do this in the setUp method, which is executed before each test, so that you need define your instance only once and have it created before each test. Then you can write your test and again the standard is to append your test name with append_test and explain what the test is doing briefly in the rest of the name. Here you are checking if the add method returns the correct result. To do this, you make use of the assertEqual method provided by the imported unittest module. This checks if the first argument is equal to the second. In this example, you are checking whether 4 is equal to the result of calling your add method on 2 and 2. In this case, the test passes as your code works and displays the following result in the terminal.

![Figure](ScreenshotsForNotes/Chapter2/Figure1.PNG)

## Following the PEP-8 Standard

As I have been introducing you to unit testing in Python, it should be clear that various patterns and standards are followed within the Python community. Some of them are enforced by tools you may wish to use, such as prepending a test name with test_ to allow runners such as Nose to find tests to execute. Others are merely standards set by Python developers to keep readability and reuse of code high as it is shared between developers. It helps to give Python code a consistent look and feel that experienced developers are familiar with, and if teams adhere to the accepted standards then when developers move to a new Python project, many aspects of the code should feel familiar.

All Python developers code should conform to the standards outlined within the PEP-8 document (available on the Python website at http://legacy.python.org/dev/peps/ pep-0008/). Guido van Rossum, creator of the Python language, along with Barry Warsaw and Nick Coghlan, writes the style guide. The document is one of the most famous PEPs (Python Enhancement Proposals) and also one of the earliest. PEPs are put forward as suggestions for changes to the language or how to use it. PEP-8 focuses on the styling of code and puts forward some of the fundamental principles when writing Python code and tests, such as:

* Indents: Four spaces for each indentation
* Maximum line length: 80 characters.
* Blank lines: Two between import, class, and function definitions. One between method definitions inside a class.
* Import statements: Should be one per line.
* Class names: Should have capitals for the first letter of each word.
* Method names: Should use all lowercase and underscores to separate words.

You should endeavor to maintain these standards and use them throughout the code you write. You will also see them followed throughout this book. You can find the whole PEP-8 document and others at www.python.org/dev/peps/. Fortunately, tools have been created to keep your code in check with the standard, such as PyLint.

## Unit Test Structure

When structuring your project, you can follow some clear standards to make your application’s code more accessible to other Python developers. These simple rules are easy to apply and result in a uniform structure to make it easy to find the test and code files you need.

* Unit tests should be placed under a test/unit directory at the top level of your project folder.
* All folders within the application’s code should be mirrored by test folders under test/unit, which will have the unit tests for each file in them. For example, app/ data should have a mirrored folder of test/unit/app/data.
* All unit test files should mirror the name of the file they are testing, with _testas the suffix. For example, app/data/data_interface.py should have a test file of test/unit/app/data/data_interface_test.py.

To illustrate these rules even more, take a look at one example of how you might structure a Flask project. Flask is the Python web framework package, which you can read more about at http://flask.pocoo.org.

![Figure](ScreenshotsForNotes/Chapter2/Figure2.PNG)

The ```__init__.py``` files indicate that the folder is a Python package so that you can import them into other Python files. For example, in app_test.py, you need to import methods from app.py so that you can test it.

You are, of course, free to structure your project however you like. This is simply a recommended structure that many developers follow.

## Making Your Life Easier with setUp

Unit testing often includes a lot of repeated code. You generally need to create instances of classes to be able to use the methods on them in multiple tests. Following good software development practices such as D.R.Y (Don’t Repeat Yourself) and Clean Code: A Handbook of Agile Software Craftsmanship by Robert Cecil Martin (Prentice–Hall, 978-0132350884), you should avoid duplicating code and keep tests as succinct as possible.

Following these principles means that changes to your tests are kept to a minimum; a mistake in duplicated code will need to be changed everywhere it was used. It also ensures your tests are easier to debug. If the test is literally executing the code it is designed to test as opposed to multiple lines of setup, then the developer will be able to clearly see the point of failure and aid in getting the problem fixed.

This is where the setUp method comes in. Although oddly named by Python conventions (it perhaps should be set_up or setup), this aspect of unit testing is powerful and minimizes the code you need to write down. Next I use the calculator example with and without the setUp method to illustrate.

![Figure](ScreenshotsForNotes/Chapter2/Figure3.PNG)

Even in this simple test case scenario, the addition of the setUp method means you only need to create the instance of Calculate once for it to be available to all test cases. Imagine how advantageous it is to be able to create this just once if you needed to test many more scenarios than just these two. Say, for example, you hadn’t used the setUp but created the Calculate class in each test case. Say your class had grown and you now had 15 test cases where this is now created. What if the initializer for Calculate changed and you now needed to pass in some new variables to the class? Instead of just one change in the setUp, you now need to change 15 lines of code.

It should be noted that even through the use of setUp, there is nothing to stop you having some test case which doesn’t make use of the objects created in the setup. Perhaps you need to test a slightly different scenario, which requires a different setUp. In this case you can just use locally created variables rather than the class level objects the setUp method will provide. This is more obvious in cases where you need to mock external libraries or calls. For example, a call to a database might need to be mocked the same way for 90% of your tests, so that would be done in the setup. You may then need to mock it differently to test an error case, which you would do in that test only, ignoring the variables created in the setup.

## Useful Methods in Unit Testing

This section provides a quick guide to all the different methods available in the unit test package. For each one, a description of its usage and an example are provided. All methods that take an optional argument, msg=None, can be provided a custom message that is displayed on failure.

### ```assertEqual(x, y, msg=None)```

This method checks to see whether argument x equals argument y. Under the covers, this method is performing the check using the == definition for the objects.

```Python3
def test_assert_equal(self):
    self.assertEqual(1, 1)
```

### ```assertAlmostEqual(x, y, places=None, msg=None, delta=None)```

On first glance, this method may seem a little strange but in context becomes useful. The method is basically useful around testing calculations when you want a result to be within a certain amount of places to the expected, or within a certain delta.

```Python3
def test_assert_almost_equal_delta_0_5(self):
    self.assertAlmostEqual(1, 1.2, delta=0.5)
    
def test_assert_almost_equal_places(self):
    self.assertAlmostEqual(1, 1.00001, places=4)
```

### ```assertRaises(exception, method, arguments, msg=None)```

Given a method and set of arguments to that method, does it raise the exception? Arguments must match the signature of the method or syntax error is raised. Arguments are passed as comma-separated lists, not as part of the method call, as shown in the following example:

```Python3
def test_assert_raises(self):
    self.assertRaises(ValueError, int, "a")
    
def test_assert_raises_alternative(self):
    with self.assertRaises(AttributeError):
        [].get
```

### ```assertDictContainsSubset(expected, actual, msg=None)```

Use this method to check whether actual contains expected. It’s useful for checking that part of a dictionary is present in the result, when you are expecting other things to be there also. For example, a large dictionary may be returned and you need to test that only a couple of entries are present.

```Python3
def test_assert_dict_contains_subset(self):
    expected = {'a': 'b'}
    actual = {'a': 'b', 'c': 'd', 'e': 'f'}
    self.assertDictContainsSubset(expected, actual)
```

### ```assertDictEqual(d1, d2, msg=None)```

This method asserts that two dictionaries contain exactly the same key value pairs. For this test to pass, the two dictionaries must be exactly the same, but not necessarily in the same order.

```Python3
def test_assert_dict_equal(self):
    expected = {'a': 'b', 'c': 'd'}
    actual = {'c': 'd', 'a': 'b'}
    self.assertDictEqual(expected, actual)
```

### ```assertTrue(expr, msg=None)```

Use this method to check the truth value of an expression or result. This method can be useful and has a few interesting caveats. This is because Python’s implicit truth behavior, such as numeric values like 0 and 1 have truth-value of False and True, respectively. Table 2-1 lists some implied truths along with test examples, but more information can be found in the Python documentation.

![Table](ScreenshotsForNotes/Chapter2/Table_2_1.PNG)

```Python3
def test_assert_true(self):
    self.assertTrue(1)
    self.assertTrue("Hello, World")
```

### ```assertFalse(expr, msg=None)```

This method is the inverse of assertTrue and is used for checking whether the expression or result under the test is False.

```Python3
def test_assert_false(self):
    self.assertFalse(0)
    self.assertFalse("")
```

### ```assertGreater(a, b, msg=None)```

This method allows you to check whether one value is greater than the other. It is essentially a helper method that wraps up the use of assertTrue on the expression a > b. It displays a helpful message by default when the value is not greater.

```Python3
def test_assert_greater(self):
    self.assertGreater(2, 1)
```

### ```assertGreaterEqual(a, b, msg=None)```

You use this method to check whether one value is greater than or equal to another value. Essentially, this wrapper is asserting True on a >= b. The assertion also gives a nicer message if the expectation is not met.

```Python3
def test_assert_greater_equal(self):
    self.assertGreaterEqual(2, 2)
```

### ```assertIn(member, container, msg=None)```

With this method, you can check whether a value is in a container (hashable) such as a list or tuple. This method is useful when you don’t care what the other values are, you just wish to check that a certain value(s) is in the container.

```Python3
def test_assert_in(self):
    self.assertIn(1, [1,2,3,4,5])
```

### ```assertIs(expr1, expr2)```

Use this method to check that expr1 and expr2 are identical. That is to say they are the same object. For example, the python code [] is [] would return False, as the creation of each list is a separate object.

```Python3
def test_assert_is(self):
    self.assertIs("a", "a")
```

### ```assertIsInstance(obj, class, msg=None)```

This method asserts that an object is an instance of a specified class. This is useful for checking that the return type of your method is as expected (for instance, if you wish to check that a value is a type of int):

```Python3
def test_assert_is_instance(self):
    self.assertIsInstance(1, int)
```

### ```assertNotIsInstance(obj, class, msg=None)```

This reverse of assertIsInstance provides an easy way to assert that the object is not a type of the class.

```Python3
def test_assert_is_not_instance(self):
    self.assertNotIsInstance(1, str)
```

### ```assertIsNone(obj, msg=None)```

Use this to easily check if a value is None. This method provides a useful standard message if not None.

```Python3
def test_assert_is_none(self):
    self.assertIsNone(None)
```

### ```assertIsNot(expr1, expr2, msg=None)```

Using this method, you can check that expr1 is not the same as expr2. This is to say that expr1 is not the same object as expr2.

```Python3
def test_assert_is_not(self):
    self.assertIsNot([], [])
```

### ```assertIsNotNone(obj, msg=None)```

This method checks that the value provided is not None. This is useful for checking that your method returns an actual value, rather than nothing.

```Python3
def test_assert_is_not_none(self):
    self.assertIsNotNone(1)
```

### ```assertLess(a, b, msg=None)```

This method checks that the value a is less than the value b. This is a wrapper method for assertTrue on a < b.

```Python3
def test_assert_less(self):
    self.assertLess(1, 2)
```

### ```assertLessEqual(a, b, msg=None)```

This method checks that the value a is less than or equal to the value b. This is a wrapper method for assertTrue on a <= b.

```Python3
def test_assert_less_equal(self):
    self.assertLessEqual(2, 2)
```

### ```assertItemsEqual(a, b, msg=None)```

This assertion is perfect for testing whether two lists are equal. Lists are unordered; therefore, assertEqual on a list can produce intermittent failing tests as the order of the lists may change when running the tests. This can produce a failing test when in fact the two lists have the same contents and are equal.

```Python3
def test_assert_items_equal(self):
    self.assertItemsEqual([1,2,3], [3,1,2])
```

### ```assertRaises(excClass, callableObj, *args, **kwargs, msg=None)```

This assertion is used to check that under certain conditions exceptions are raised. You pass in the exception you expect, the callable that will raise the exception and any arguments to that callable. In the earlier example, this pops the first item from an empty list and results in an IndexError.

```Python3
def test_assert_raises(self):
    self.assertRaises(IndexError, [].pop, 0)
```

# 3. Utilizing Unit Test Tools

## Mocking a Class and Method Response

Creating a mock is fairly simple. You simply need to import the Mock class and then create an instance of it. You can then attach methods to the mock that you want to return some value. Create a test file called mock_example_test.py and use the following code.

```Python3
import unittest
from mock import Mock


class TestMocking(unittest.TestCase):
    def test_mock_method_returns(self):
        my_mock = Mock()
        my_mock.my_method.return_value = "hello"
        self.assertEqual("hello", my_mock.my_method())


if __name__ == '__main__':
    unittest.main()
```

In this example, you can create an instance of the mock named my_mock, add the my_method to it, and state that when it is called, it should return the string "hello".

You may now wonder how this is useful when testing your application. Suppose you have a program that looks up accounts from a database. If that account class is initialized using a data_interface class to call a database for the account information, then instead of providing a real data_interface you can instead mock the data_interface and provide the methods and return values you need for your test. Because the data_interface class is a whole other class with set responsibilities, the testing for this class should be assumed as handled elsewhere. To that end, the mock data_interface will just be set up to have a dummy method on it and return whatever you like when it is called. This allows you to set up the scenarios and use cases of the code as required, such as returning a value successfully for an account or returning some error case.

To illustrate this example with some code, your simple Account class may look something like this:

```Python3
class Account:
    def __init__(self, data_interface):
        self.di = data_interface

    def get_account(self, id_num):
        return self.di.get(id_num)
```

The class has just one method that returns the data obtained from the database related to the provided ID number. Now write a test to check that the data is returned correctly for ID 1 given the data that you set up in the mock data_interface. Create a test file called account_test.py and try the following code:

```Python3
import unittest
from mock import Mock
from account import Account


class TestAccount(unittest.TestCase):
    def test_account_returns_data_for_id_1(self):
        account_data = {
            "id": 1,
            "name": "test"
        }

        mock_data_interface = Mock()
        mock_data_interface.get.return_value = account_data

        account = Account(mock_data_interface)

        self.assertDictEqual(account_data, account.get_account(1))


if __name__ == '__main__':
    unittest.main()
```

By passing in the mock_data_interface in this way, you can create the scenario you need to exercise only the Account class without testing any of the functionality provided by the data_interface class


# 4. Writing Testable Documentation

\-
