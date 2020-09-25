# KnockMail
Copyright 2018 KnockMail

Written originally by: * **Alisson Moretto** - [4w4k3](https://github.com/4w4k3)

Twitter: @4w4k3Official

Python3 fork maintained by: * **Spencer Heywood** - [heywoodlh](https://github.com/heywoodlh)

Docker Installation by: * **Sion Smith** - [sionsmith](https://github.com/sionsmith)

![Main](https://github.com/4w4k3/KnockMail/blob/master/Screens/snap.png)
### Installation:
```
git clone https://github.com/4w4k3/KnockMail.git
```

```
cd KnockMail
```

```
docker build -t knockmail .
```

### Running:


For an interactive menu: 
```
docker run knockmail
```

Validate single e-mail address:
```
docker run knockmail --email example@example.com
```

Validate emails stored in text file:
```
docker run knockmail --file /path/to/inputfile.txt
```


### Screen
![SearchFile](https://github.com/4w4k3/KnockMail/blob/master/Screens/snap02.png)

## DISCLAIMER: 

"DISCLAIMED. IN NO EVENT SHALL THE COPYRIGHT HOLDER OR CONTRIBUTORS BE LIABLE
FOR ANY DIRECT, INDIRECT, INCIDENTAL, SPECIAL, EXEMPLARY, OR CONSEQUENTIAL
DAMAGES (INCLUDING, BUT NOT LIMITED TO, PROCUREMENT OF SUBSTITUTE GOODS OR
SERVICES; LOSS OF USE, DATA, OR PROFITS; OR BUSINESS INTERRUPTION) HOWEVER
CAUSED AND ON ANY THEORY OF LIABILITY, WHETHER IN CONTRACT, STRICT LIABILITY,
OR TORT (INCLUDING NEGLIGENCE OR OTHERWISE) ARISING IN ANY WAY OUT OF THE USE
OF THIS SOFTWARE, EVEN IF ADVISED OF THE POSSIBILITY OF SUCH DAMAGE."
Taken from [LICENSE](LICENSE).

### Tested on:

+ Kali Linux - SANA
+ Kali Linux - ROLLING
+ Ubuntu 14.04-16.04 LTS
+ Debian 8.5
+ Linux Mint 18.1
+ OS X High Sierra

### Contribute:
Send me more features if you want it :D

**I need your help to make it become better.**

### Contact:
**4w4k3@protonmail.com**

## License:

This project is licensed under the BSD-3-Clause - see the [LICENSE](LICENSE) file for details.
