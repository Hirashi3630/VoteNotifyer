<h1 align="center">VoteNotifyer</h1>
<p>
  <img alt="Version" src="https://img.shields.io/badge/version-0.0.1-blue.svg?cacheSeconds=2592000" />
  <a href="https://www.mit-license.org" target="_blank">
    <img alt="License: MIT" src="https://img.shields.io/badge/License-MIT-yellow.svg" />
  </a>
</p>

> VoteNotifyer is program to help you remind when you can vote for Minecraft servers such as [minecraftservers.org](https://minecraftservers.org/), [minecraft-mp.com](https://minecraft-mp.com/) and many more...
>
> * **Supported servers**:
>   * [czech-craft.eu](https://czech-craft.eu/)

#### Screenshots:

![preview_1](https://user-images.githubusercontent.com/37778278/85880577-862cea00-b7dc-11ea-9f08-18097b5c8f6f.jpg)

## Install

#### Without [git](https://git-scm.com)

Choose this option if you want pure source and you're not going to contribute to the repo.

To download source code this way [click here](https://github.com/Hirashi3630/VoteNotifyer/archive/master.zip).

#### With [git](https://git-scm.com)

```shell script
git clone https://github.com/Hirashi3630/VoteNotifyer.git
```
or with pip
```shell script
pip install git+https://github.com/Hirashi3630/VoteNotifyer.git@[master or other branch]
```

## Usage

1. edit `config.json` ([how?](https://github.com/Hirashi3630/VoteNotifyer#config))
2. run `python MCNotifyer.py`

## Config

default `config.json` file can be found [here](https://raw.githubusercontent.com/Hirashi3630/VoteNotifyer/master/config.json)

<details>

* **"repeat-interval"** -  As soon as you can vote, the program will notify you every **X** second
    * type: `int` _(number)_
    * default: `5` - it will notify you every fifth second
    * disabled: `-1`
* **"scraper-file"** - Name of scraper script file (without `.py`)
    * type: `string` _(text)_
    * default: `czech-craft-eu` 
    * disabled: N/A
* **"scraper-file-par"** - Parameter for scraper file (currently used for server name)
    * type: `string` _(text)_
    * default: `skymc` 
    * disabled: N/A
* **"sound-path"** - Path to sound file that will play if you can vote. [freesound.org](https://freesound.org/) is one of many good sites for sound effects. For example [this](https://freesound.org/people/morrisjm/sounds/268756/).
    * type: `string` _(text)_
    * default: `sfx/notif01.wav` 
    * disabled: `-1`
* **"open-browser"** - Once you can vote, open a voting site in your default browser
    * type: `boolean` _(true/false)_
    * default: `false` 
    * disabled: `false`

</details>

## Author

**Hirashi3630**

* Github: [@Hirashi3630](https://github.com/Hirashi3630)
* Discord: Hirashi#3630

## Contributing

Contributions, issues and feature requests are welcome!<br />Feel free to check [issues page](https://github.com/Hirashi3630/VoteNotifyer/issues). 

_btw this code is shit_

## License

This project is [MIT](https://github.com/Hirashi3630/VoteNotifyer/blob/master/LICENSE) licensed.