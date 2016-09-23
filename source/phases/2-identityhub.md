ARPA2 phase 2: IdentityHub
==========================

>   *The IdentityHub phase provides a management console for users, over which
>   they can create identities for users, groups, roles, pseudonyms.*

This is the second phase of ARPA2, and it is targeted at delivering an
identity control cockpit, including every bit of cryptography that can
be used to prove those identities.  The IdentityHub supports Kerberos,
X.509 certificates and OpenPGP keys.

But that's not all.  The IdentityHub hinges on a
[Bring Your Own Identity](http://internetwide.org/blog/2015/04/22/id-2-byoid.html)
idea, where you have an identity under your local domain that you should
be able to bring anywhere you go online.  Well, anywhere supportive of
the InternetWide Architecture, of course.  Still, there are other
initiatives, and we seek to support those too, as well as possible
and wherever it is not harmful to end user privacy and security.

This means that anyone could potentially see who you are, and link your
behaviours throught that one identity.  In protection of your identity,
we therefore support the use of
[aliases, pseudonyms, roles and groups](http://internetwide.org/blog/2015/04/23/id-3-idforms.html),
all helpful to control how you appear to those parties with which you
engage in online contact.

All this may sound straightforward enough, but let us assure you that
there are quite a few technical problems to be resolved.  Enough to
making it quite a challenge.  The reason we take this on is that we
have set ourselves the goal of redesigning the whole thing, without
limiting ourselves to the confines of an individual interest group;
[history has shown](http://internetwide.org/blog/2015/04/21/id-1-intro.html)
that individual interests make it difficult to come to something
that benefits the Internet as a whole.

Are we arrogant for undertaking this?  Perhaps.
Do we stand a chance?  Certainly... we see many organisations, some
very large, gasp at the extent of what the IdentityHub wants to do,
and fall in love with it.  The general response comes down to
*you are doing something that we hold dear... but if we did it,
we would be forced to confine ourselves to just this little corner*.
It does seem that adding up all those individual corners leads pretty
much to what the IdentityHub does though, so we have good hopes for
broad support.

*If anyone can do this, it will be the open source community!*

Parties preparing to
[adopt the IdentityHub](../starting)
are advised to do the following:

  * Use Kerberos for authentication
  * Use the TLS Pool for authentication where possible
  * Use Diameter or, failing that, use RADIUS for authorisation

The general naming scheme for IdentityHub will be the
[DoNAI](http://donai.arpa2.net),
meaning domain-or-user-at-domain.
We have defined
[Selectors](http://donai.arpa2.net/selector.html)
to be used as a kind of wildcard matches, and
[Access Control Lists](http://donai.arpa2.net/acl.html)
to derive relationships.

In order to establish
[realm crossover](http://realm-xover.arpa2.net),
meaning the mechanism that an identity from one security realm can authenticate
to another, we have found that the
[Kerberos variety](http://realm-xover.arpa2.net/kerberos.html)
is the most probable road to success, chiefly because it only requires changes
in centrally controlled components.  Having said that, there are no reasons
to block things like
[OpenID Connect](http://realm-xover.arpa2.net/openid.html)
or even
[OAuth](http://realm-xover.arpa2.net/oauth.html)
but they are each facing problems -- such as that everyone wants to play
the role of identity provider, while nobody wants to be on the trusting end
of the game.

It is however vital for personal control to be in charge of the identity
provider component.  If anything should be hosted by ourselves, it is the
cornerstone for deciding *this session may enter on behalf of Charles* --
and that is quadrupally true on an Internet where identity providers have
second thoughts about the privacy of their users.


