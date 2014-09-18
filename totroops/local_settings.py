# Settings for local host.
import dj_database_url

DATABASES = {
    'default': dj_database_url.config(default='postgres://ph652925:password@localhost/template1')
}
