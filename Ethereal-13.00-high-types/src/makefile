# Ethereal is a UCI chess playing engine authored by Andrew Grant.
# <https://github.com/AndyGrant/Ethereal>     <andrew@grantnet.us>
#
# Ethereal is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# Ethereal is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with this program.  If not, see <http://www.gnu.org/licenses/>.

CC   = gcc
SRC  = *.c
LIBS = -lpthread -lm
EXE  = Ethereal

ifdef EVALFILE
    NN = -DUSE_NNUE=1 -DEVALFILE=\"$(EVALFILE)\"
else
    NN = -DUSE_NNUE=0
endif

WFLAGS   = -std=gnu11 -Wall -Wextra -Wshadow
RFLAGS   = -Os -s $(WFLAGS) $(NN) -DNDEBUG -flto -static
CFLAGS   = -Os -s $(WFLAGS) $(NN) -DNDEBUG -flto -march=native
TFLAGS   = -Os -s $(WFLAGS) $(NN) -DNDEBUG -flto -march=native -fopenmp -DTUNE
PGOFLAGS = -Os -s $(WFLAGS) $(NN) -DNDEBUG -flto -march=native -fno-asynchronous-unwind-tables

POPCNTFLAGS = -DUSE_POPCNT -msse3 -mpopcnt
PEXTFLAGS   = $(POPCNTFLAGS) -DUSE_PEXT -mbmi2
AVX2FLAGS   = -msse -msse3 -mpopcnt -mavx2 -msse4.1 -mssse3 -msse2

ARMV8FLAGS  = -Os -s $(WFLAGS) -DNDEBUG -flto -march=armv8-a -m64
ARMV7FLAGS  = -Os -s $(WFLAGS) -DNDEBUG -flto -march=armv7-a -m32
ARMV7FLAGS += -mfloat-abi=softfp -mfpu=vfpv3-d16 -mthumb -Wl,--fix-cortex-a8

popcnt:
	$(CC) $(CFLAGS) $(SRC) $(LIBS) $(POPCNTFLAGS) -o $(EXE)

nopopcnt:
	$(CC) $(CFLAGS) $(SRC) $(LIBS) -o $(EXE)

pext:
	$(CC) $(CFLAGS) $(SRC) $(LIBS) $(PEXTFLAGS) -o $(EXE)

release:
	mkdir ../dist
	$(CC) $(RFLAGS) $(SRC) $(LIBS) -o ../dist/$(EXE)$(VER)-x64-nopopcnt.exe
	$(CC) $(RFLAGS) $(SRC) $(LIBS) $(POPCNTFLAGS) -o ../dist/$(EXE)$(VER)-x64-popcnt.exe
	$(CC) $(RFLAGS) $(SRC) $(LIBS) $(PEXTFLAGS) -o ../dist/$(EXE)$(VER)-x64-pext.exe
	$(CC) $(RFLAGS) $(SRC) $(LIBS) $(AVX2FLAGS) $(POPCNTFLAGS) -o ../dist/$(EXE)$(VER)-x64-popcnt-avx2.exe
	$(CC) $(RFLAGS) $(SRC) $(LIBS) $(AVX2FLAGS) $(PEXTFLAGS) -o ../dist/$(EXE)$(VER)-x64-pext-avx2.exe

tune:
	$(CC) $(TFLAGS) $(SRC) $(LIBS) $(POPCNT) -o $(EXE)

pgo:
	rm -f *.gcda
	$(CC) -fprofile-generate $(PGOFLAGS) $(SRC) $(LIBS) $(POPCNTFLAGS) -o $(EXE)
	./$(EXE) bench
	$(CC) -fprofile-use $(PGOFLAGS) $(SRC) $(LIBS) $(POPCNTFLAGS) -o $(EXE)
	rm -f *.gcda

pgopext:
	rm -f *.gcda
	$(CC) -fprofile-generate $(PGOFLAGS) $(SRC) $(LIBS) $(PEXTFLAGS) -o $(EXE)
	./$(EXE) bench
	$(CC) -fprofile-use $(PGOFLAGS) $(SRC) $(LIBS) $(PEXTFLAGS) -o $(EXE)
	rm -f *.gcda

armv8:
	$(CC) $(ARMV8FLAGS) $(SRC) -lm -o $(EXE)

armv7:
	$(CC) $(ARMV7FLAGS) $(SRC) -lm -o $(EXE)
