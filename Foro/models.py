from django.db import models
from django.contrib.auth.models import User

POST_TYPE_CHOICES = (
    ('text', 'Texto'),
    ('image', 'Imagen'),
    ('video', 'Video'),
)

REACTION_CHOICES = (
    ('like', 'Like'),
    ('love', 'Love'),
    ('haha', 'Haha'),
    ('wow', 'Wow'),
    ('sad', 'Sad'),
    ('angry', 'Angry'),
    ('poop', 'Poop'),
)


class Foro(models.Model):
    autor = models.ForeignKey(
        User,
        related_name="foros",
        on_delete=models.CASCADE
    )
    titulo = models.CharField(max_length=200)
    contenido_texto = models.TextField(blank=True)
    imagen = models.ImageField(upload_to="foro/images/", blank=True, null=True)
    video = models.FileField(upload_to="foro/videos/", blank=True, null=True)
    post_type = models.CharField(
        max_length=10,
        choices=POST_TYPE_CHOICES,
        default="text"
    )
    reposted = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.titulo

    # PROPIEDADES para contar reacciones del Foro
    @property
    def like_count(self):
        return self.reactions.filter(reaction_type='like').count()

    @property
    def love_count(self):
        return self.reactions.filter(reaction_type='love').count()

    @property
    def haha_count(self):
        return self.reactions.filter(reaction_type='haha').count()

    @property
    def wow_count(self):
        return self.reactions.filter(reaction_type='wow').count()

    @property
    def sad_count(self):
        return self.reactions.filter(reaction_type='sad').count()

    @property
    def angry_count(self):
        return self.reactions.filter(reaction_type='angry').count()

    @property
    def poop_count(self):
        return self.reactions.filter(reaction_type='poop').count()


class Reaction(models.Model):
    foro = models.ForeignKey(
        Foro,
        related_name="reactions",
        on_delete=models.CASCADE
    )
    user = models.ForeignKey(
        User,
        related_name="reactions",
        on_delete=models.CASCADE
    )
    reaction_type = models.CharField(
        max_length=20,
        choices=REACTION_CHOICES
    )
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.user.username} -> {self.reaction_type} -> {self.foro.titulo}"


class Comentario(models.Model):
    foro = models.ForeignKey(
        Foro,
        related_name="comentarios",
        on_delete=models.CASCADE
    )
    autor = models.ForeignKey(
        User,
        related_name="comentarios",
        on_delete=models.CASCADE
    )
    contenido = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Comentario por {self.autor.username} en {self.foro.titulo}"

    # PROPIEDADES para contar reacciones del Comentario
    @property
    def like_count(self):
        return self.reactions.filter(reaction_type='like').count()

    @property
    def love_count(self):
        return self.reactions.filter(reaction_type='love').count()

    @property
    def haha_count(self):
        return self.reactions.filter(reaction_type='haha').count()

    @property
    def wow_count(self):
        return self.reactions.filter(reaction_type='wow').count()

    @property
    def sad_count(self):
        return self.reactions.filter(reaction_type='sad').count()

    @property
    def angry_count(self):
        return self.reactions.filter(reaction_type='angry').count()

    @property
    def poop_count(self):
        return self.reactions.filter(reaction_type='poop').count()


class CommentReaction(models.Model):
    comentario = models.ForeignKey(
        Comentario,
        related_name="reactions",
        on_delete=models.CASCADE
    )
    user = models.ForeignKey(
        User,
        related_name="comment_reactions",
        on_delete=models.CASCADE
    )
    reaction_type = models.CharField(
        max_length=20,
        choices=REACTION_CHOICES
    )
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.user.username} -> {self.reaction_type} -> CommentID {self.comentario.pk}"
