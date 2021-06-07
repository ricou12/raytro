# raytro
# Application de gestion de rétrospective

La rétrospective est une des dernières étapes d'un sprint Scrum. C'est l'occasion de recueillir les retours des membres de l'équipe


## Les fonctionnalités


### Création de compte

Tout utilisateur doit d'abord créer un compte avec :

- prénom
- mail (qui servira de pseudo)
- mot de passe


### Connexion

Un utilisateur doit pouvoir se connecter avec son mail/pass pour accéder à toutes les autres fonctionnalités de l'application


### Création d'un feedback (utilisateur authentifié)

Si un utilisateur n'a pas encore saisi de feedback durant la semaine en cours, il est invité à renseigner au moins un "j'ai aimé" ET un "je n'ai pas aimé" (il peut en saisir plusieurs de chaque).

Chaque avis est émis de manière totalement anonyme : il ne faut pas que l'on puisse savoir qui a saisi quel avis, par quel moyen que ce soit.

Une fois que l'utilisateur a saisi et qu'il valide, il faut lui demander une confirmation avant l'enregistrement effectif. Les saisies étant anonymes, il ne sera pas possible de les modifier/supprimer. Il restera possible de venir en ajouter d'autres cependant.

### Afficher les feedbacks (utilisateur authentifié)

Une fois qu'un utilisateur a participé au feedback de la semaine en cours, il peut afficher la liste de tous les feedbacks saisis cette semaine.
Ils doivent apparaitre sous forme de deux listes distinctes.


### Tenir un état des participations par semaine (administrateur authentifié)

Pour supporter la fonctionnalité précédente, il faut tenir un état des participations par semaine : chaque semaine débute avec aucun membre de l'équipe ayant participé, puis tout en conservant l'anonymat, il faut noter qu'une personne a participé lorsque c'est le cas.

Cette liste ne doit être consultable que par les administrateurs pour des raisons évidentes d'anonymat.


## Livrables

Chaque équipe sera constituée de 3 à 4 personnes.

- Un apprenant à distance par groupe maximum
- Pas de groupe constitué exclusivement d'apprenant sortant de la même formation (DWWM)

Vous devez dans un premier temps modéliser la base de données :

> Vous fournirez un MCD et/ou un MLD de votre base ainsi qu'un script de création au format SQL (base MySQL ou Postgres)

Vous produirez ensuite une maquette sommaire des pages suivantes :

- saisie d'un feedback
- affichage des feedbacks

> Vous fournirez les captures d'écran commentées ainsi que les fichiers au format source (ou lien dans le cas de réalisation sur une webapp comme Figma ou Marvel avec un accès public, sans avoir à créer des comptes pour accéder aux productions)

Une application frontend et une application backend (qui peuvent n'être qu'une seule et même application si vous le souhaitez) implémentant les fonctionnalités décrites en première partie et basées sur la BDD modélisée ainsi que sur le design proposé.

Vous vous accorderez sur les technologies à utiliser, avec un seul développement par équipe.

> Vous fournirez le code de votre/vos application(s) dans un dépôt Git public (plateforme de votre choix : Gitlab, Bitbucket, Azure DevOps, Github, etc.)
>
> - Chaque application de votre dépôt doit contenir un `readme.md` contenant une description sommaire de votre application, au moins deux captures d'écran ainsi que la procédure permettant de la déployer (technologies utilisées, etc.)
> - Votre code sera commenté (chaque fichier ET fonction auront un *docblock*)
> - Le code le plus à jour devra se trouver sur la branche `master` de votre dépôt
> - **bonus** : si vous pouvez créer un ou deux tests unitaires et expliquer comment les utiliser, vous serez exceptionnel(le)s !


