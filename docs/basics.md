# Django basics

Django is a framework to develop websites. _It is not a server!_

## Details

Django follows the Model View Template (MVT):

- _Model_: handles all the data interactions (database).
- _View_: its the intermediate element between the client and the host, basically
  is the element responsible to choose and control what the user will see. It
  receives a HTTP request and decides what to do based on that request. In
  simple terms, the view is a function (could be a class too) that receives
  a HTTP request and must return a HTTP response.
- _Template_: The actual element that will be shown to the user, in this case
  an html file. Try to not do any logic in this for it will be easier to test
  and handle things.

We do not work directly in the `project/` directory. Django uses apps to separate
the whole application in little pieces to better organize and manage all the
components. The organization and separation of a piece of the application
into apps is totally developer charged, you decide how the apps will look like
and how they will be separated.
