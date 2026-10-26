# Migrations

Migrations are Django's way of propagating model changes into the database.
So everytime you want to apply changes you make to your database, you have to
propagate these migrations.

To apply the changes made on our models we use the `migrate` command to commit
these changes. When you create new migrations (new models), we use the
`makemigrations` command to create new migration files and then apply them with
`migrate` again.

When you make a migration you create a file inside the project `migrations`
folder. Generally, we do not edit these files, we make a new migration (a new
file) to apply new changes of your models.
