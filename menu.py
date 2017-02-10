from database import Database
from models.blog import Blog


class Menu(object):
    def __init__(self):
        # Ask user for author name
        self.user = input("Enter your author name: ")
        self.user_blog = None
        # Check if they've already got an account
        if self._user_has_account():
            print("Welcome back, {}".format(self.user))
        # If not, prompt to create one
        else:
            self._prompt_user_for_account()

    # underscore indicates a private method to be called by this class only
    def _user_has_account(self):
        """Checks if user has an account by searching DB for a blog with author=self.user
        If so, assign this blog to self.user blog and return True. Otherwise, return False"""
        blog = Database.find_one(collection='blogs', query={'author': self.user})
        if blog is not None:
            self.user_blog = Blog.from_mongo(blog['id'])
            return True
        else:
            return False

    def _prompt_user_for_account(self):
        """Creates a new user by creating a blog with self.user as an author"""
        title = input("Enter blog title: ")
        description = input("Enter blog description: ")
        blog = Blog(author=self.user,
                    title=title,
                    description=description)
        blog.save_to_mongo()
        self.user_blog = blog

    def run_menu(self):
        # Ask user - read or write blogs?
        read_or_write = input("Do you want to read (R) or write (W) blogs? ")
        if read_or_write == "R":
            self._list_blogs()
            self._view_blog()
        elif read_or_write == "W":
            self.user_blog.new_post()
        else:
            print("Thank you for blogging!")

    @staticmethod
    def _list_blogs():
        blogs = Database.find(collection='blogs',
                              query={})
        for blog in blogs:
            print("ID: {}, Title: {}, Author: {}".format(blog['id'], blog['title'], blog['author']))

    @staticmethod
    def _view_blog():
        blog_to_see = input("Enter the ID of the blog you'd like to see: ")
        blog = Blog.from_mongo(id=blog_to_see)
        posts = blog.get_posts()
        for post in posts:
            print("Date: {}, title: {}\n\n{}".format(post['created_date'], post['title'], post['content']))


