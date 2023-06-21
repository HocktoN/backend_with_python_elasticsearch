from api.elasticsearch_create_index.elastic import User
from elasticsearch_dsl import Search


class UserService:

    @classmethod
    def create(cls, **kwargs):
        user = User(username=kwargs['username'], email=kwargs['email'], password=kwargs['password'])
        user.save()
        return user.to_dict(include_meta=True)

    @classmethod
    def get(cls, username):
        response = Search(using='default').index('users').query("match", username=username).execute()
        hits = response.hits
        user = [hit.to_dict() for hit in hits][0]
        return user

    @classmethod
    def update(cls, username, **kwargs):
        response = Search(using='default').index('users').query("match", username=username).execute()
        hits = response.hits
        for hit in hits:
            user_id = hit.meta.id
            user = User.get(id=user_id)
            user.username = kwargs['username']
            user.email = kwargs['email']
            user.password = kwargs['password']
            user.save()
        return kwargs

    @classmethod
    def delete(cls, username):
        response = Search(using='default').index('users').query("match", username=username).execute()
        hits = response.hits
        for hit in hits:
            user_id = hit.meta.id
            User.get(id=user_id).delete()
        return hits[0].to_dict() if hits else None


